import sys
import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore, init


init()
title2 = """ 
                                         _,aggdd888bbgg,,_
                                    ,ad88888YYYYYYYYYYY8888ba,
                                 ,d888P""'              ``""Y88b,
                               ,d888"'                       "Y888,
                              d88P'                            `Y88b,
                            ,d88'                                `Y88,
                           ,888'                                  `Y88,
                          ,d88'                                    `Y8b,
                          d88'                                      `88I
                         ,88P            IP lookup(ErrorIP)          I88
                         I88I          By Eyesaq - Eyesaq#6969       I88
                         I88I                                        I8I
                         `888,                                       d8I
                          `888,                                     d88'
                           `888,                                   d8PI
                           ,dP"8b,                               ,8P'd'
                         ,dP'   "Yb,                          _,d8" P'
                       ,dP' ,db,  "Yb,_                    ,ad8P" ,P'
                     ,dP' ,d8888b,  `"Yba,,__        __,ad88P"  ,d"
                   ,dP' ,d88888888b,    "88Y8888888888PP""   _,d"
                 ,dP' ,d888888888888P  ,d"8              _,gd"'
               ,dP' ,d888888888888P' ,d" ,8bbaagggggaaddP""'
             ,dP' ,d888888888888P' ,d" ,d"'
           ,dP' ,d888888888888P' ,d" ,d"
         ,dP' ,d888888888888P' ,d" ,d"     
       ,dP' ,d888888888888P' ,d" ,d"       
     ,dP' ,d888888888888P' ,d" ,d"
   ,dP' ,d888888888888P' ,d" ,d"
 ,dP' ,d888888888888P' ,d" ,d"
dP'  d888888888888P' ,d" ,d"
8"Ya, `888888888P' ,d" ,d"
8  "Ya, `88888P' ,d" ,d"
8a,  "Ya, `8P' ,d" ,d"
 "Ya,  "Ya,  ,d" ,d"
   "Ya,  "Y8P" ,d"
     "Ya,  8 ,d"
       "Ya,8d"
         "YP"""
print(Fore.LIGHTRED_EX + title2)
import urllib.request as urllib2
import json

while True:

            ip = input(Fore.LIGHTRED_EX + "enter the IP you want to lookup: ")
            url = "http://ip-api.com/json/"
            response = urllib2.urlopen(url + ip)
            data = response.read()
            values = json.loads(data)

            print(Fore.GREEN + "IP: " + str(values['query']))
            print(Fore.GREEN + "Status: " + str(values['status']))
            print(Fore.GREEN + "Country: " + str(values['country']))
            print(Fore.GREEN + "Country Code: " + str(values['countryCode']))
            print(Fore.GREEN + "Region: " + str(values['region']))
            print(Fore.GREEN + "Region Name: " + str(values['regionName']))
            print(Fore.GREEN + "City: " + str(values['city']))
            print(Fore.GREEN + "Zip Code: " + str(values['zip']))
            print(Fore.GREEN + "Latitude: " + str(values['lat']))
            print(Fore.GREEN + "Longitude: " + str(values['lon']))
            print(Fore.GREEN + "Timezone: " + str(values['timezone']))
            print(Fore.GREEN + "Isp: " + str(values['isp']))
            print(Fore.GREEN + "Organization: " + str(values['org']))
            print(Fore.GREEN + "As: " + str(values['as']))