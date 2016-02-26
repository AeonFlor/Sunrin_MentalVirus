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

def search(dirname):
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
					print(full_filename)
	except PermissionError:
		print("ERROR : Permission\n")

if __name__ == '__main__':
	print("Score : %d\n"%score)
	while score<30:
		if game() == 1:
			search("Y:\Documents\\test\\")

