try:
	import requests as network
	import os as pc
	from colorama import Fore, Back, Style
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
	
def ngocok():
	linux = 'clear'
	windows = 'cls'
	
	pc.system([linux,windows][pc.name == 'nt'])
	
	mer = Fore.RED
	hij = Fore.GREEN
	kun = Fore.YELLOW
	
	# Variable Warna Background
	
	bmer = Back.RED
	bhij = Back.GREEN
	bkun = Back.YELLOW
	
	# Reset All Style Warna
	
	reset = Style.RESET_ALL
	
	# Banner
	
	banner = """
	{}
/$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$           
| $$  | $$|__  $$__/|__  $$__/| $$__  $$          
| $$  | $$   | $$      | $$   | $$  \ $$ /$$   /$$
| $$$$$$$$   | $$      | $$   | $$$$$$$/|  $$ /$$/
| $$__  $$   | $$      | $$   | $$____/  \  $$$$/ 
| $$  | $$   | $$      | $$   | $$        >$$  $$ 
| $$  | $$   | $$      | $$   | $$       /$$/\  $$
|__/  |__/   |__/      |__/   |__/      |__/  \__/
	
{}{}( ! ) HTTP STATUS SCANNER!
	{}""".format(hij,bhij,mer,reset)
	print(banner)
	
	
def GetStatus(site):
	site = listnya.strip()
	try:
		if 'http://' not in site:
			check = network.get(site)
			if ('200' in str(check.status_code)):
				print(Fore.GREEN+f"{site} STATUS CODE : \033[0m[ \33[32;1m200 \033[0m]")
				open("200.txt", 'a').write(site + "\n")
			elif ('403' in str(check.status_code)):
				print(Fore.GREEN+f"{site} STATUS CODE : \033[0m[ \33[0;36m403 \033[0m]")
				open("403.txt", 'a').write(site + "\n")
			elif ('404' in str(check.status_code)):
				print(Fore.GREEN+f"{site} STATUS CODE : \033[0m[ \33[1;33m404 \033[0m]")
				open("404.txt", 'a').write(site + "\n")
	
		elif 'http://' or 'https://' in site:
			rep = site.replace('http://', '').replace('https://', '').replace('/', '')
			check2 = network.get(rep)
			if ('200' in str(check2.status_code)):
				print(Fore.GREEN+f"{site} STATUS CODE : \033[0m[ \33[32;1m200 \033[0m]")
				open("200.txt", 'a').write(site + "\n")
			elif ('403' in str(check2.status_code)):
				print(Fore.GREEN+f"{site} STATUS CODE : \033[0m[ \33[0;36m403 \033[0m]")
				open("403.txt", 'a').write(site + "\n")
			elif ('404' in str(check2.status_code)):
				print(Fore.GREEN+f"{site} STATUS CODE : \033[0m[ \33[1;33m404 \033[0m]")
				open("404.txt", 'a').write(site + "\n")
			
	
	except:
		pass
	
ngocok()
list = str(input("Masukan List Domain \33[32;1m> \033[0m"))
	
try:
	with open(list) as f:
		for listnya in f:
			GetStatus(listnya)
	
except IOError as err:
	exit(f'\n [\033[1;35m>\033[0m] file {err} error/nggak ada')