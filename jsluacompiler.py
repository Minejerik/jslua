import os
filename = input('Name of jslua file?\n')
outputfile = input('Name of output file?\n')
f = open(filename, 'r')
data = f.read()
datalist = data.split('\n')
f.close()
f = open(outputfile, 'w')


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def erro(string, loc):
	print(bcolors.FAIL + string + ' error on line ', loc, bcolors.ENDC)
	exit()


def main():
	os.system('clear')
	toadd = ''
	print('Running Compiler')
	mcommentbegin = False
	mcommentend = False
	mcbeginline = 0
	mcendline = 0
	for i in range(0, len(datalist)):
		temp = datalist[i]
		temp = temp.replace('--', '..')
		temp = temp.replace('import(', 'require(')
		if temp != '':
			if temp[0] + temp[1] == '|~':
				print('Multi line Comment begin')
				temp = temp.replace('|~', '--[[')
				toadd = toadd + temp + '\n'
				mcommentbegin = True
				mcbeginline = i
			elif temp[0] + temp[1] == '~|':
				print('Multi line comment end')
				temp = temp.replace('~|', '--]]')
				toadd = toadd + temp + '\n'
				mcommentend = True
				mcendline = i
			elif temp[0] == '~':
				print('Commenting on replacment')
				temp = temp.replace('~', '--')
				toadd = toadd + temp + '\n'
			elif 'if' in temp:
				print('Replacing If')
				if not ';' in temp:
					erro('Expected symbol ";"', i)
				temp = temp.replace(';', '')
				temp = temp.replace('{', ' then')
				toadd = toadd + temp + '\n'
			elif 'while' in temp:
				print('While Looping')
				if not ';' in temp:
					erro('Expected symbol ";"', i)
				temp = temp.replace(';', '')
				temp = temp.replace('{', '')
				toadd = toadd + temp + ' do \n'
			elif 'function' in temp:
				print('Function Replaced')
				if not ';' in temp:
					erro('Expected symbol ";"', i)
				temp = temp.replace(';', '')
				temp = temp.replace('{', ' ')
				toadd = toadd + temp + '\n'
			elif temp[0] == '}':
				print('Adding End')
				toadd = toadd + 'end \n'
			else:
				if not mcommentbegin == True and mcommentend == False:
					if not ';' in temp:
						erro('Expected symbol ";"', i)

				temp = temp.replace(';', '')
				toadd = toadd + temp + '\n'
		else:
			toadd = toadd + ''
	print('Checking multiline comments')
	if mcommentbegin == True and mcommentend == False:
		erro("Missing end comment!", mcbeginline + 1)
	elif mcommentend == True and mcommentbegin == False:
		erro("Missing begining comment!", mcendline + 1)
	f.write(toadd)
	f.close()
	print('Compiled ' + filename + ' into ' + outputfile)
main()