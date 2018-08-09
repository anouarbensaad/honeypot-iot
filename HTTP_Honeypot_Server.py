#!/usr/bin/env python

# Title : Router_Honeypot
# Author: BENSAAD Anouar

import socket
import time
import sys
import mysql.connector
import MySQLdb
import signal
import getpass

colors = True # Output should be colored
machine = sys.platform # Detecting the os of current system

if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False # Colors shouldn't be displayed in mac & windows
if not colors:
    end = red = white = green = yellow = run = bad = good = info = que = ''
else:

    end = '\033[1;m'
    red = '\033[91m'
    white = '\033[1;97m'
    green = '\033[1;32m'
    yellow = '\033[1;33m'
    run = '\033[1;97m[~]\033[1;m'
    bad = '\033[1;31m[-]\033[1;m'
    good = '\033[1;32m[+]\033[1;m'
    info = '\033[1;33m[!]\033[1;m'
que = '\033[1;34m[?]\033[1;m'


MSGLEN = 1024
dbconn = None
server_sock = None

def myreceive(c):

    chunks = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        data = c.recv(min(MSGLEN - bytes_recd, 2048))
        if not data: break
        chunks.append(data)
        bytes_recd = bytes_recd + len(data)
    return ''.join(chunks)

def process_request(c,addr,datainput):

	global dbconn
	try:
		cursor = dbconn.cursor()
		timestr = time.strftime("%Y/%m/%d-%H/%M/%S")
		data = datainput.decode('utf-8')
		list = data.split(' ')
		method = list[0]
		requested_file = list[1]
                print ('Method: ', method)
		
		if (data == 'OPTIONS / HTTP/1.0') :
			c.send(server_banner) 
		
		current_time = time.strftime("%Y/%m/%d-%H:%M:%S")
		ip_hacker = addr
		# FUCNTION INSERT INTO MYSQL
		#aa = str(current_time)
		#bb = str(ip_hacker)
		#cc = str(addr)
		#log = (aa, bb, cc)
		#cursor.execute("""INSERT INTO log (datetime, iphacker, uri) VALUES (%s, %s, %s)""",log);
		#con.commit()

		print  '%s Time:'% red,current_time, ' Hacker: ', ip_hacker 
		print  '%s Bad guy is looking for : \n\r'% white,end,data 

		with open('Sys/log/Client Data', 'a') as file :
                   file.write(timestr +'Informations :' +str(data)+'\n')

		file = requested_file.split('?')[0]
		file = file.lstrip('/')
		if (file == ''):
		 	file = 'sign.html'
		if (file =='admin.php'):
			file = 'sign.html'

		try:
                  file_handler = open(file,'rb')

                  response = file_handler.read()

                  file_handler.close()

                  header = 'HTTP/1.1 200 OK\n'
		  if(file.endswith(".jpg")):

            	    extension = 'image/jpg'

        	  elif(file.endswith(".css")):

            	    extension = 'text/css'

        	  else:

            	     extension = 'text/html'


        	  header += 'Content-Type: '+str(extension)+'\n\n'
                except Exception as e:

                  header = 'HTTP/1.1 404 not found \n\n'
 		  response = '<html><body><p>Error 404: not found</p></body></html>'		
 		  	
 		  		#/Sys/log/File Requested : Hacker URI Tracing

		with open('Sys/log/File Requested', 'a') as file :
           	   file.write(timestr +'Body request :' +str(requested_file)+'\n')
		
                # FUCNTION INSERT INTO MYSQL
                aa = str(current_time)
                bb = str(ip_hacker)
                cc = str(requested_file)
                log = (aa, bb, cc)
                cursor.execute("""INSERT INTO log (date, iphacker, uri) VALUES (%s, %s, %s)""",log);
                dbconn.commit()

    		reponse_finale = header.encode('utf-8')
		reponse_finale += response
		c.send(reponse_finale)
	except Exception, e:
		print e

#FUNCTION CLOSING SERVER IF U TYPING Ctrl+C.
def signal_handler(sig, frame):
	global server_sock
	server_sock.shutdown(socket.SHUT_RDWR)
	print('You pressed Ctrl+C!')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
	
def Main():


#Just Banner
	print("%s  _          _   ____           _   _                        " % white)
	print("%s (_)___  ___| |_/ ___|  ___    | | | | ___  _ __   ___ _   _ " % white)
	print("%s | / __|/ _ \ __\___ \ / _ \   | |_| |/ _ \| '_ \ / _ \ | | |" % white)
	print("%s | \__ \  __/ |_ ___) | (_) |  |  _  | (_) | | | |  __/ |_| |" % red)
	print("%s |_|___/\___|\__|____/ \___/___|_| |_|\___/|_| |_|\___|\__, |" % red)
	print("%s                          |_____|                      |___/ " % end)

	#Global Variable.
	global dbconn, server_sock
	timestr = time.strftime("%Y/%m/%d-%H/%M/%S")
 	print '\nLogin Request '
 	
 	password = "123"
 	username = "isetadmin"
	
	#DataBase Connect
	dbconn = MySQLdb.connect("localhost", "root", "isetso", "isetsohoney")
	
 	user_in = raw_input('Username : ')
 	user_input = getpass.getpass('Password : ')
 	
 	#/Sys/log/login, PWD : Hacker Try of Login & Password
 	with open('Sys/log/login, PWD','a') as file :
       		file.write(timestr +'\n' +'LOGIN: ' +str(user_in)+'\n' +'PWD: '+str(user_input)+'\n')
    #Administrator Condition Connexion.
 	if  user_input != password or user_in != username  :
 	#Warning File, Administrator Typing Fault.
           with open('Warning', 'a+r') as file :
 	    file.write(timestr + '**** Warning **** : It is a Brute Force:'  +str(user_in) +'/' +str(user_input))
           sys.exit('%s Incorrect Password, terminating... \n' % bad)

 	print '%s Connexion avec Succes' % good
 	#Socket Connexion
	server_sock = socket.socket()
	server_name = ''
	server_port = 999
	#Banner of IoT : Router
	server_banner = """Sagem F@st 2604 ADSL router linux 7 3.49a4G_Topnet
  | banner: \xFF\xFD\x01\xFF\xFD!\xFF\xFB\x01\xFF\xFB\x03FAST2604 ADSL Rout
  |_er (Software Version:3.49a4G_Topnet)\x0D\x0ALogin:
  Service Info: Device: broadband router """
	server_sock.bind((server_name, server_port))
	header = ''
	#Server Running.
	print '%s Starting Server ON' % run, server_name, server_port

	server_sock.listen(5)
	try:
		while 1:
			data = None
			(c,addr) = server_sock.accept()
			try:
				data = myreceive(c)
			except socket.error, ex:
				print ex
			if data : process_request(c,addr,data)
			c.close()
	except Exception, ex:
		print ex
		server_sock.close()
 

if __name__== '__main__' :
        Main ()
