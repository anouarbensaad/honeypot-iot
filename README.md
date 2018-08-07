# HTTP-Honeypot
This tool to simulate http server attacks in Python which logs HackerIP and all the tracing he does into a Logfile then a database.

#Requirements

* Python (2.7 or 3.0)
* Apache2
* Mysql-server
* HTTrack

#Installation

* Clone the repository. `git clone https://github.com/anouarbensaad/HTTP-Honeypot.git` and switch into the directory `cd HTTP-Honeypot`

#Configuration DATABASE

* Run mysql with root user `sudo mysql -u root`
* Create the database isetsohoney `CREATE DATABASE isetsohoney;`
* add the privileges to root`GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'isetso';`
* create table log with this fields`CREATE TABLE log (id int NOT NULL PRIMARY KEY, date datetime, iphacker varchar(255), uri varchar(255));`

#Running

* run server with command : `python HTTP_Honeypot_Server.py`
* Starting Server ON `999`, Username : `root` , Password : `toor`
* Run `HTTrack` for copy real websites to local directory and copy it in `Sys/fake`

#Test

* Scan The Server Banner with Nmap
`nmap -sV --script=banner 192.168.1.1 -p999`
* Open 
`http://192.168.1.1:999`
`
