#!/usr/bin/env python
#
# auto-sslscan.py version 0.4
#
# https://github.com/attackdebris/auto-sslscan
#
# Base code credit: https://github.com/DanMcInerney/nmap-parser/blob/master/nmap-parser.py 
#

import os
import subprocess
import sys
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException

instructions =  "auto-sslscan - v0.4 ( https://github.com/attackdebris/auto-sslscan )\n" +\
                "\nUSAGE: auto-sslscan.py [nmap-ouput.xml] [output-file]" 

if len(sys.argv) <3 or sys.argv[1] == "-h" or sys.argv[1] == "--h" or sys.argv[1] == "-help" or sys.argv[1] == "--help":
        print(instructions)
        sys.exit()
elif len(sys.argv) >3:
        print (instructions)
        sys.exit()
elif len(sys.argv) ==3:
        nmapxml = sys.argv[1]
        myfile = sys.argv[2]
        with open(myfile, 'w') as f:
                f.write("====================================================================\n")
                f.write("auto-sslscan - v0.4 ( https://github.com/attackdebris/auto-sslscan )\n")
                f.write("====================================================================\n\n")
        temp = ".tmp-auto-sslscan"
        sslservices = myfile.replace('.txt', '') + "-ssl-services.txt"
        with open(temp, 'w'):
                pass
        with open(sslservices, 'w'):
                pass 
        print("auto-sslscan - v0.4 ( https://github.com/attackdebris/auto-sslscan )\n")

def report_parser(report):
        ''' Parse the Nmap XML report '''
        for host in report.hosts:
                ip = host.address

                # Get the port and service
                # objects in host.services are NmapService objects
                for s in host.services:
                # Check if port is open
                        if s.open():
                                serv = s.service
                                port = s.port
                                tunnel = s.tunnel

                        # Perform some action on the data
                                print_data(ip, port, tunnel)


def print_data(ip, port, tunnel):
        ''' Do something with the nmap data '''
        if tunnel != '':
                with open(temp, 'w') as f:
                        f.write('{0}:{1}\n'.format(ip, port))
                print('Performing sslscan of {0}:{1}'.format(ip, port))
                with open(sslservices, 'a+') as f:
                        f.write('{0}:{1}\n'.format(ip, port))
                with open(myfile, 'a+') as f:
                        subprocess.call(["sslscan", "--no-failed", "--targets=" + temp], stdout=f)

def end():
        print("\nsslscan results saved to: {}".format(myfile))
        print("SSL services list saved to: {}".format(sslservices))
        os.remove(temp)


def main():
    report = NmapParser.parse_fromfile(nmapxml)
    report_parser(report)
    end()

main()
