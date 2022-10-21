import os
import time

filename = 'main.jslua'  #input('Name of jslua file?\n')
outputfile = 'main.lua'  #input('Name of output file?\n')
f = open(filename, 'r')
data = f.read()
datalist = data.split('\n')
f.close()
f = open(outputfile, 'w')
var = {}
varup = {}
usedsleep = False
sleepscript = '''local clock = os.clock
function sleep(n)
local t0 = clock()
while clock() - t0 <= n do end
end\n'''

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
	loc += 1
	print(bcolors.FAIL + string + '	on line ', loc, bcolors.ENDC)
	exit()

def warn(string, loc):
	loc += 1
	print(bcolors.WARNING+string+' on line ', loc, bcolors.ENDC)


def main():
	usedsleep = False
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
		temp = temp.replace('};', 'end;')
		temp = temp.replace('import(', 'require(')
		temp = temp.replace('read(','io.read(').replace('pr(','print(').replace('wi(','io.write(').replace('lcl ','local ').replace('exit(','os.exit(')
		trueline = i
		if trueline % 20 == 0:
			toadd = toadd + '--COMPILED USING MINEJERIK JSLUA COMPILER\n'
			print('adding signature')
		if temp != '' and temp != 'end':
			if '|~' in temp:
				print('Multi line Comment begin')
				toadd = toadd
				mcommentbegin = True
				mcbeginline = i
			elif '~|' in temp:
				print('Multi line comment end')
				toadd = toadd
				mcommentend = True
				mcendline = i
			elif temp[0] == '~':
				print('Commenting on replacment')
				toadd = toadd
			elif 'repeat for ' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"', i)
				print('repeating for')
				temp = temp.replace('{;','').replace('repeat for ','')
				if temp == '' or temp ==' ':
					erro('Requires Arguments',i)
				temp = 'for i = 1,'+str(temp)+',1 do'
				toadd = toadd + temp + '\n'
			elif 'js.sleep' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"', i)
				print('sleeping peacfully')
				usedsleep = True
				temp = temp.replace('js.sleep(','sleep(').replace(';','')
				toadd = toadd +temp +'\n'
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
			elif 'gbl' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"', i)
				temp = temp.replace('gbl ', '')
				templet = temp.find(' ', 0, len(temp))
				templet = temp[0:int(templet)]
				var[len(var) + 1] = templet
				varup[len(varup) + 1] = templet.upper()
				temp = temp.replace(';','')
				toadd = toadd + temp + '\n'
				print(templet + " variable indexed")
			elif 'tbl' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"', i)
				temp = temp.replace('tbl ', '')
				templet = temp.find(' ', 0, len(temp))
				templet = temp[0:int(templet)]
				var[len(var) + 1] = templet
				varup[len(varup) + 1] = templet.upper()
				toadd = toadd + temp + '}\n'
				print(templet + " variable indexed")
			else:
				if not mcommentbegin == True and mcommentend == False:
					if temp != '};':
						if not ';' in temp:
							if temp != 'end':
								erro('Expected symbol ";"', i)
					else:
						toadd = toadd + 'end\n'
						print('end')
					temp = temp.replace(';', '')
					toadd = toadd + temp + '\n'
		else:
			toadd = toadd + ''
	print('Checking multiline comments')
	if mcommentbegin == True and mcommentend == False:
		erro("Missing end comment!", mcbeginline)
	elif mcommentend == True and mcommentbegin == False:
		erro("Missing begining comment!", mcendline)
	toadd = toadd.replace('}', '')
	for i in range(1, len(var) + 1):
		print('Replacing ' + var[i] + ' with ' + varup[i])
		toadd = toadd.replace(var[i], varup[i])
	toadd = toadd.replace('[];','{}')
	if usedsleep == True:
		f.write(sleepscript)
	f.write(toadd)
	f.close()
	print(bcolors.OKGREEN + 'Compiled ' + filename + ' into ' + outputfile +
	      bcolors.ENDC)
	print('quitting in 5')
	time.sleep(5)
	exit()
main()