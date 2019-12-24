#!/usr/bin/env python

import subprocess

interface = input("Interface > ")
new_mac = input("New MAC address > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac + "...")

subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("sudo ifconfig wlan0 up", shell=True)

