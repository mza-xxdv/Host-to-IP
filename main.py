import socket
import requests
import os
from bs4 import BeautifulSoup

'''
To check IP vps?
To check hostname vpn server?
OK

'''

red = '\033[91m' #merah
green = '\033[92m' #hijau
cyan = '\033[96m' #cyan
blank = '\033[0m' #default

def validIPAddress(IP):
    """
    :type IP: str
    :rtype: str
    """

    def isIPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(s):
        if len(s) > 4:
            return False
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False

    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
        return "IPv6"
    return "Neither"


versionfo = cyan+ r'''
    ______                     __   ________ 
   / ____/________ ___  ______/ /  /  _/ __ \
  / /_  / ___/ __ `/ / / / __  /   / // /_/ /
 / __/ / /  / /_/ / /_/ / /_/ /  _/ // ____/ 
/_/   /_/   \__,_/\__,_/\__,_/  /___/_/     
                                             
  by mza-xxdv -- v0.01 -- Telegram : @E_9mm  
'''+blank

def get_ip_address():
    while True:
        try:
            host = input("[+] Host or Domain Name: ")
            ip_address = socket.gethostbyname(host)
            return host, ip_address
        except socket.error:
            print(f"{red}Host is invalid or unreachable.{blank}")


def get_ip_info(ip_address):
    reqview = requests.get(f"http://ip-api.com/json/{ip_address}").json()
    isp = reqview['as']
    country = reqview['country']
    region_name = reqview['regionName']
    city = reqview['city']
    timezone = reqview['timezone']

    endpoint = f"https://scamalytics.com/ip/{ip_address}"

    try:
        r = requests.get(endpoint)
        htmlresponse = r.text
        soup = BeautifulSoup(htmlresponse, 'html.parser')
        coderet = soup.find_all(class_="panel_title high_risk")
        finalstuff = str(coderet)
        amb = str(finalstuff.split("\">")[1].split("</")[0])
        coderet = str(soup.find_all(class_="panel_body"))
        coderet1 = str(soup.find_all(class_="score"))

        print('=====================================')
        print('        IP Address Information       ')
        print('=====================================')
        print('IP\t : ' + ip_address)
        print('ISP\t : ' + isp)
        print('City\t : ' + city)
        print('Region\t : ' + region_name)
        print('Country\t : ' + country)
        print('Timezone : ' + timezone)
        print('=====================================')
        print('FraudInfo')
        print(amb + ' ; ' + coderet1.replace('[<div class="score">','').replace('</div>]','/100'))
        print("")
        print('If unsure, please check the manual')
        print(f'https://scamalytics.com/ip/{ip_address}')
        print(os.linesep)
        print('====Response Info')
        print(coderet.replace('[<div class="panel_body">','').replace('<b>','').replace('</b>','').replace('Scamalytics','We').replace('</div>]','').replace('  ',' '))
        print('====END')
        cek_lagi()

    except:
        try:
            if (finalstuff.find("private IP address.")):
                print("The IP Address you provided is local and not a public one. Please refer to https://www.h3xed.com/web-and-internet/whats-the-difference-between-external-and-local-ip-addresses for more info")
            else:
                print("Connection Error, This program needs internet to function.")
        except:
            print("Unknown Error Occurred, Possibly Network Restrictions.")

def cek_lagi():
        pilihan = input("\nDo you want to check again? (y/t): ")
        if pilihan.lower() == "y":
            main()
        elif pilihan.lower() == "t":
            print("\nSee You!")
        elif pilihan.lower() == "n":
            print("\nSee You!")
        else:
            print("\nInvalid choice. Please select the correct option.\n")
            cek_lagi()

def main():
    print(versionfo)
    host, ip = get_ip_address()
    print(f"{green}IPv4 Address for {host}: {ip}{blank}\n")

    pilihan_scamalytics = input("Would you like to check it out in Scamalytics? (y/n): ")
    if pilihan_scamalytics.lower() == "y":
        get_ip_info(ip)
    elif pilihan_scamalytics.lower() == "t":
        print("\nSee You!")
    elif pilihan_scamalytics.lower() == "n":
        print("\nSee You!")
    else:
        print("Invalid choice. Please select the correct option.")

if __name__ == "__main__":
    main()
