#!/usr/bin/env python
# Title : HTTP_Honeypot
# Author: BENSAAD Anouar
import socket
import time
import sys
import mysql.connector
import MySQLdb
def Main():
	timestr = time.strftime("%Y/%m/%d-%H/%M/%S")
 	print '\nLogin Request \n'
 	
 	password = "toor"
 	username = "root"
	
	#DATABASE CONNECT
	
	con = MySQLdb.connect("localhost", "root", "isetso", "isetsohoney")
	cursor = con.cursor()
	
	#ROOT , #TOOR
 	
	user_in = raw_input('Please Enter username: ')
 	user_input = raw_input('Please Enter Password: ')
 	
	#Make Directory File and touch file Login, PWD [Sys/log/login, PWD]
	#Login, PWD : This File For Hacker Trying & URI
	
	with open('Sys/log/login, PWD','a') as file :
       		file.write(timestr +'\n' +'LOGIN: ' +str(user_in)+'\n' +'PWD: '+str(user_input)+'\n')

 	if  user_input != password or user_in != username  :

           with open('Warning', 'a+r') as file :
 	    file.write(timestr + '**** Warning **** : It is a Brute Force:'  +str(user_in) +'/' +str(user_input))
           sys.exit('Incorrect Password, terminating... \n')

 	print 'User is logged in!\n' 
 
	#DEFAULT : socket.AF_INET ,socket.SOCK_STREAM
	
	s = socket.socket()
	server_name = ''
	
	#Port Listning 999
	
	server_port = 999
	
	#Real Router Banner , For Scanning Nmap
	#nmap -sV --script=banner @ip -p999
	
	server_banner = """Sagem F@st 2604 ADSL router linux 7 3.49a4G_Topnet
  | banner: \xFF\xFD\x01\xFF\xFD!\xFF\xFB\x01\xFF\xFB\x03FAST2604 ADSL Rout
  |_er (Software Version:3.49a4G_Topnet)\x0D\x0ALogin:
  Service Info: Device: broadband router """
	
	s.bind((server_name, server_port))
	
	header = ''
	print 'Starting Server ON', server_name, server_port

	s.listen(5)
	while True:

    		c,addr = s.accept()
    		data = c.recv(1024).decode('utf-8')
		list = data.split(' ')
		method = list[0]
		requested_file = list[1]
                print ('Method: ', method)
		
		#if scanning .. send the server banner.
		#if data == "http","HTTP/1.0","GET","bind","version","OPTIONS"
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

		print  'TIME:',current_time, ' HACKER: ', ip_hacker
		print  'Bad guy is looking for :',addr, data

		#Make Directory File and touch file Client Data [Sys/log/Client Data]
		#Client Data : This File For Hacker Infromations
		
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
		#Make Directory File and touch file File Requested [Sys/log/File Requested]
		with open('Sys/log/File Requested', 'a') as file :
           	   file.write(timestr +'Body request :' +str(requested_file)+'\n')
		
                # FUCNTION INSERT INTO MYSQL
                aa = str(current_time)
                bb = str(ip_hacker)
                cc = str(requested_file)
                log = (aa, bb, cc)
                cursor.execute("""INSERT INTO log (date, iphacker, uri) VALUES (%s, %s, %s)""",log);
                con.commit()

    		reponse_finale = header.encode('utf-8')
		reponse_finale += response
		c.send(reponse_finale)


    		c.close()
 

if __name__== '__main__' :

        Main ()

