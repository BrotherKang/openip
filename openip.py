#! python3
# -*- coding: utf-8 -*-

import os
import sys
import webbrowser
import time

def main():
    run_scan()

def run_scan():
    
    IePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(IePath):
        IePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser(IePath))
    
    with open("target.txt","r") as file_IP:
        ip_content = file_IP.readlines()
    
    ipCount = len(ip_content)
    if (ipCount % 10 == 0):
        ipLoop_count = int(ipCount // 10)
    else:
        ipLoop_count = int(ipCount // 10) + 1

    IpList = [x.strip() for x in ip_content] 
    
    for round in range(0,ipLoop_count):
        for line0 in IpList[(round * 10):((round + 1) * 10)]:
            if line0.strip().endswith('443'):
                urlIP = "https://" + line0.strip()
            else:
                urlIP = "http://" + line0.strip()

            webbrowser.get("Chrome").open_new_tab(urlIP)

            time.sleep(1)

        print("Press Enter-key to contuine...")
        input()

    print("Press Enter-key to EndApp ^_^")
    input()

if __name__ == "__main__":
    main()
