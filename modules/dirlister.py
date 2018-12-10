import os

def run(**args):
	print("[*] IN dirlister modules.")
	files = os.listdir(".")

	return str(files)
