#!/usr/bin/env python

import subprocess
import optparse

# Implementing OptionParser class for parser object instance
parser = optparse.OptionParser()
# New command line arguments
parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address of..")
parser.add_option("-m", "--mac", dest="mac", help="New MAC address..")

parser.parse_args()

interface = input("Interface > ")
mac = input("New MAC address > ")

print("[+] Changing MAC address for " + interface + " to " + mac + "...")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])
