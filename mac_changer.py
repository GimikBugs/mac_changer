#!/usr/bin/env python

import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:55"

print("[+] Changing MAC for " + interface)

subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("sudo ifconfig wlan0 up", shell=True)

print("[+] " + interface + " has been changed to " + new_mac)