from colorama import Fore
import os
import sys
import subprocess
import xml.etree.ElementTree as ET



banner = F"""


 _______  _______ _________ _______  _______  _         _____  
(  ____ \(  ___  )\__   __/(  ___  )(  ____ \( (    /| / ___ \ 
| (    \/| (   ) |   ) (   | (   ) || (    \/|  \  ( |( (   ) )
| |      | |   | |   | |   | (___) || (_____ |   \ | | \/  / / 
| | ____ | |   | |   | |   |  ___  |(_____  )| (\ \) |    ( (  
| | \_  )| |   | |   | |   | (   ) |      ) || | \   |    | |  
| (___) || (___) |   | |   | )   ( |/\____) || )  \  |    (_)  
(_______)(_______)   )_(   |/     \|\_______)|/    )_)     _   
                                                          (_) 
{Fore.MAGENTA}
by: c0d3ninja


"""

print(f"{Fore.WHITE}{banner}")
print(f"{Fore.RESET}")

if os.geteuid() != 0:
    print(f"{Fore.RED}This script must be run as root!")
    sys.exit()

def scan(command: str) -> str:
    cmd = command
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = p.communicate()
    out = out.decode() 
    return out

try:
    scan(f"./asnmap -a {sys.argv[1]} -silent > iprange.txt")
    scan(f"sudo masscan -p80,443,8080,8443 -iL iprange.txt --rate=10000 -oX ip_addr.xml")

    tree = ET.parse("ip_addr.xml")
    root = tree.getroot()

    ip_addrs = []
    for data in root.iter('address'):
        ip = data.get('addr')
        print(f"{Fore.WHITE}{ip}")
        ip_addrs.append(ip)

    with open("ip_addr.txt", "a") as f:
        for ips in ip_addrs:
            f.writelines(f"{ips}\n")
except IndexError:
    print(f"{Fore.RED}You must enter an argument")
    sys.exit()

except KeyboardInterrupt:
        print("\nProgram interrupted.")
        exit(0)

