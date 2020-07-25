import re

print("Regex teszt")
ipcim = input("Ip cím: ")

egyezik = re.match(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$', ipcim)

if egyezik:
	print("Egyezik")
else:
	print("Nem egyezik")



