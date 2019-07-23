# wifi_plug is a python script made to automate installation of wifi penetration tools
# I don't own any of the used tools, but i thank their authors very much
# Written by @x_Freed0m
import os
import socket
import subprocess
import sys
from subprocess import STDOUT

from termcolor import colored

apt_pkgs = ['aircrack-ng', 'wifite', 'ettercap', 'sslstrip', 'isc-dhcp-server',
            'dhcp-server', 'dsniff', 'reaver', 'bully', 'asleap', 'bettercap',
            'mdk4', 'hostapd', 'lighttpd', 'hostapd-wpe']  # packages from
# apt-get
git_pkgs = ['https://github.com/v1s1t0r1sh3r3/airgeddon.git',
            'https://github.com/wi-fi-analyzer/fluxion.git',
            'https://github.com/gobiasinfosec/Wireless_Query.git',
            'https://github.com/H0nus/RogueSploit.git',
            'https://github.com/P0cL4bs/WiFi-Pumpkin.git',
            'https://github.com/wifiphisher/wifiphisher.git',
            'https://github.com/s0lst1c3/eaphammer.git',
            'https://github.com/entropy1337/infernal-twin.git',
            'https://github.com/OpenSecurityResearch/hostapd-wpe.git',
            'https://github.com/chrizator/netattack.git',
            'https://github.com/hkm/whoishere.py.git',
            'https://github.com/InfamousSYN/rogue.git',
            'https://github.com/sensepost/mana.git',
            'https://github.com/elkentaro/KismetMobileDashboard.git',
            'https://github.com/wpatoolkit/Cap-Converter.git',
            'https://github.com/tehw0lf/airbash.git',
            'https://github.com/hashcat/hashcat-utils.git']


# Packages from github


def internet_check(host="8.8.8.8", port=53, timeout=5):  # checking the host has internet connection
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print colored("[+] Internet access verified, moving forward", 'green')
        return True
    except Exception as ex:
        print colored("[-] Can't connect to the internet.\n" + ex.message, 'red')
        sys.exit(1)


def installer():
    if internet_check():
        try:
            print colored("[*] Updating the repositories...", 'green')
            os.system('apt-get update')
            print colored('[*] Done updating', 'green')
        except KeyboardInterrupt:
            print colored("[-]halted by CTRL+C", 'red')
            sys.exit(1)
        for pkg in apt_pkgs:  # installing apt-get packages
            try:
                print colored("[*] Installing " + pkg, 'green')
                proc = subprocess.Popen('apt-get install -y ' + pkg, shell=True, stdin=None,
                                        stdout=open(os.devnull, "wb"), stderr=STDOUT,
                                        executable="/bin/bash")
                proc.wait()
                print colored("[+] Done installing " + pkg + " moving forward...")
            except KeyboardInterrupt:
                print colored("[-]halted by CTRL+C", 'red')
                sys.exit(1)
        for pkg in git_pkgs:  # installing github packages
            try:
                proc = subprocess.Popen("git clone " + pkg, shell=True, stdin=None,
                                        stdout=open(os.devnull, "wb"), stderr=STDOUT,
                                        executable="/bin/bash")
                proc.wait()
                print colored("[+] Done cloning " + pkg, 'green')
            except KeyboardInterrupt:
                print colored("[-]halted by CTRL+C", 'red')
                sys.exit(1)
            print colored("[+] All done! have fun!", 'green')
            sys.exit(0)
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
