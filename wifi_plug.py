# wifi_plug is a python script made to automate installation of wifi penteration tools
# I don't own any of the used tools, but i thank their authors very much
# Written by @x_Freed0m
import os
import sys
from subprocess import STDOUT, check_call, Popen
import shlex, subprocess
import socket
from termcolor import colored
import signal


apt_pkgs = ['aircrack-ng', 'wifite'] # packages from apt-get
git_pkgs = ['https://github.com/v1s1t0r1sh3r3/airgeddon/archive/master.zip', 'https://github.com/wi-fi-analyzer/fluxion/archive/master.zip', 'https://github.com/gobiasinfosec/Wireless_Query/archive/master.zip', 'https://github.com/H0nus/RogueSploit/archive/master.zip', 'https://github.com/P0cL4bs/WiFi-Pumpkin/archive/master.zip', 'https://github.com/wifiphisher/wifiphisher/archive/master.zip', 'https://github.com/s0lst1c3/eaphammer/archive/master.zip', 'https://github.com/entropy1337/infernal-twin/archive/master.zip', 'https://github.com/OpenSecurityResearch/hostapd-wpe/archive/master.zip', 'https://github.com/chrizator/netattack/archive/master.zip', 'https://github.com/hkm/whoishere.py/archive/master.zip', 'https://github.com/InfamousSYN/rogue/archive/master.zip', 'https://github.com/sensepost/mana/archive/master.zip', 'https://github.com/elkentaro/KismetMobileDashboard/archive/master.zip', 'https://github.com/wpatoolkit/Cap-Converter/archive/master.zip', 'https://github.com/tehw0lf/airbash/archive/master.zip', 'https://github.com/hashcat/hashcat-utils/archive/master.zip'] # packges from github

def internet_check(host="8.8.8.8", port=53, timeout=5): # checking the host has internet connection
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print colored("[+] Internet access verified, moving forward" ,'green')
        return True
    except Exception as ex:
        print colored("[-] Can't connect to the internet.\n" + ex.message, 'red')
        return False
        sys.exit(1)

def installer():
    if internet_check() == True:
        try:
            print colored("[*] Updating the repositories...", 'green')
            os.system('apt-get update')
            print colored('[*] Done updating', 'green')
        except KeyboardInterrupt:
            print colored("[-]halted by CTRL+C", 'red')
            sys.exit(1)
        for pkg in apt_pkgs: # installing apt-get packages
            try:
                print colored("[*] Installing "+ pkg, 'green')
                proc = subprocess.Popen('apt-get install -y ' + pkg, shell=True, stdin=None, stdout=open(os.devnull, "wb"), stderr=STDOUT, executable="/bin/bash")
                proc.wait()
                print colored("[+] Done installing " + pkg + " moving forward...")
            except KeyboardInterrupt:
                print colored("[-]halted by CTRL+C", 'red')
                sys.exit(1)
        for pkg in git_pkgs: # installing github packages
            try:
                proc = subprocess.Popen("wget " + pkg, shell=True, stdin=None, stdout=open(os.devnull, "wb"), stderr=STDOUT, executable="/bin/bash")
                proc.wait()
                proc = subprocess.Popen('unzip master.zip', shell=True, stdin=None, stdout=open(os.devnull, "wb"), stderr=STDOUT, executable="/bin/bash")
                proc.wait()
                proc = subprocess.Popen('rm master.zip', shell=True, stdin=None, stdout=open(os.devnull, "wb"), stderr=STDOUT, executable="/bin/bash")
                print colored("[+] Done downloading and extracting " + pkg, 'green')
            except KeyboardInterrupt:
                print colored("[-]halted by CTRL+C", 'red')
                sys.exit(1)
            print colored("[+] All done! have fun!", 'green')
    else:
        print colored("[-] Can't connect to the internet.\n", 'red')

def help():
    print "This script will use apt-get in order to install"
    print "some wifi testing tools"
    print "Thanks to ALL the related tools authors, I don't own any of them!"
    print "Written by @x_Freed0m"
    print "\nUsage: "
    print "python wifi_plug.py"
    sys.exit()

def main():
    if len(sys.argv) == 1:
        installer()
    else:
        help()

if __name__ == '__main__':
     main()