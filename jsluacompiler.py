import os

def find_files(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

def loading(i):
	porcent = i/len(datalist)*100
	os.system('cls')
	print (int(porcent),'Percent Done')

filename = 'main.jslua' #input('Name of jslua file?\n')
outputfile = 'main.lua' #input('Name of output file?\n')
f = open(filename, 'r')
data = f.read()
datalist = data.split('\n')
f.close()
f = open(outputfile, 'w')
var = {}
varup = {}
printlater = {}
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


def erro(string,line,loc):
	loc += 1
	print(bcolors.FAIL +string + '	on line ', loc,'\n'+line+' <--', bcolors.ENDC)
	exit()

def errold(string,loc):
	loc += 1
	print(bcolors.FAIL +string + '	on line ', loc, bcolors.ENDC)
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
		temp = temp.replace('read(','io.read(').replace('pr(','print(').replace('wi(','io.write(').replace('lcl ','local ').replace('exit(','os.exit(').replace('ran(','math.random(')
		loading(i+1)
		trueline = i
		if trueline % 20 == 0:
			toadd = toadd + '--COMPILED USING MINEJERIK JSLUA COMPILER\n'
		if temp != '' and temp != 'end':
			if '|~' in temp:
				toadd = toadd
				mcommentbegin = True
				mcbeginline = i
			elif '~|' in temp:
				toadd = toadd
				mcommentend = True
				mcendline = i
			elif temp[0] == '~':
				toadd = toadd
			elif 'repeat for ' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"',temp, i)
				temp = temp.replace('{;','').replace('repeat for ','')
				if temp == '' or temp ==' ':
					errold('Requires Arguments',i)
				temp = 'for i = 1,'+str(temp)+',1 do'
				toadd = toadd + temp + '\n'
			elif 'js.sleep' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"',temp, i)
				usedsleep = True
				temp = temp.replace('js.sleep(','sleep(').replace(';','')
				toadd = toadd +temp +'\n'
			elif 'if' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"',temp, i)
				temp = temp.replace(';', '')
				temp = temp.replace('{', ' then')
				toadd = toadd + temp + '\n'
			elif 'while' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"',temp, i)
				temp = temp.replace(';', '')
				temp = temp.replace('{', '')
				toadd = toadd + temp + ' do \n'
			elif 'function' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"',temp, i)
				temp = temp.replace(';', '')
				temp = temp.replace('{', ' ')
				toadd = toadd + temp + '\n'
			elif 'gbl' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"',temp, i)
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
					erro('Expected symbol ";"',temp, i)
				temp = temp.replace('tbl ', '')
				templet = temp.find(' ', 0, len(temp))
				templet = temp[0:int(templet)]
				var[len(var) + 1] = templet
				varup[len(varup) + 1] = templet.upper()
				toadd = toadd + temp + '}\n'
				print(templet + " variable indexed")
			elif 'import(' in temp:
				if not ';' in temp:
					erro('Expected symbol ";"',temp, i)
				tempe = temp.replace('import(','').replace(')','').replace('"','').replace("'",'').replace(';','')
				tempe = tempe + '.jslua'
				file = find_files(tempe,os.getcwd())
				if file != []:
					printlater[i] = 'Remember to compile '+tempe
				if file == []:
					printlater[i] = tempe+' not found at line '+str(i)
				temp = temp.replace('import(','require(').replace(';','')
				toadd = toadd + temp +'\n'
			else:
				if not mcommentbegin == True and mcommentend == False:
					if temp != '};':
						if not ';' in temp:
							if temp != 'end':
								erro('Expected symbol ";"',temp, i)
					else:
						toadd = toadd + 'end\n'
						print('end')
					temp = temp.replace(';', '')
					toadd = toadd + temp + '\n'
		else:
			toadd = toadd + ''
	if mcommentbegin == True and mcommentend == False:
		errold("Missing end comment!", mcbeginline)
	elif mcommentend == True and mcommentbegin == False:
		errold("Missing begining comment!", mcendline)
	toadd = toadd.replace('}', '')
	for i in range(1, len(var) + 1):
		print('Replacing ' + var[i] + ' with ' + varup[i])
		toadd = toadd.replace(var[i], varup[i])
	toadd = toadd.replace('[];','{}')
	if len(printlater)>0:
		for i in range(1,len(printlater)):
			print(printlater[i])
	if usedsleep == True:
		f.write(sleepscript)
	f.write(toadd)
	f.close()
	print(bcolors.OKGREEN + 'Compiled ' + filename + ' into ' + outputfile +
	      bcolors.ENDC)
	print('Press enter to quit!')
	input()
	exit()
main()