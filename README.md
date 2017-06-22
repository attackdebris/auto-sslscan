# Auto-sslscan

Auto-sslscan is a python script designed to automate the process of conducting ssl scanning via sslcan (https://github.com/rbsec/sslscan).

The Auto-sslscan script parses an nmap.xml output file, extracts all SSL services and automatically performs an sslscan of them.


## Installation

git clone https://github.com/attackdebris/auto-sslscan.git

### Prerequisites 

The only pre-reqs are:

1. You must have sslscan installed and in your path (default in Kali)
2. You need a valid Nmap XML output file (see below)

### Nmap XML File

The Nmap XML file must have been created with version scanning enabled i.e. via Nmap flags `-sV` or `-A` (see below) 

```bash
nmap -A -p 443 -iL targets.txt -oX nmap-output.xml 
nmap -sS -sV -p 443 -iL targets.txt -oX nmap-output.xml
```

## Usage

```bash
/auto-sslscan.py 
auto-sslscan - v0.1 ( https://github.com/attackdebris/auto-sslscan )

USAGE: auto-sslscan.py [nmap-ouput.xml] [output-file]
```

### Example
```bash
./auto-sslscan.py attackdebris.xml outfile.txt
auto-sslscan - v0.1 ( https://github.com/attackdebris/auto-sslscan )

Performing sslscan of 185.176.90.16:443
Performing sslscan of 199.101.100.186:443

sslscan results saved to: outfile.txt
SSL services list saved to: ssl-services.txt
```
