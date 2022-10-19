filename = input('Name of jslua file?\n')
outputfile = input('Name of output file?\n')
f = open(filename, 'r')
data = f.read()
datalist = data.split('\n')
f.close()
f = open(outputfile, 'w')


def main():
	toadd = ''
	print('Running Compiler')

	for i in range(0, len(datalist)):
		temp = datalist[i]
		temp = temp.replace(';', '')
		temp = temp.replace('--', '..')
		temp = temp.replace('import(', 'require(')
		if temp != '':
			if temp[0] == '~':
				print('Commenting on replacment')
				temp = temp.replace('~', '--')
				toadd = toadd + temp + '\n'
			elif 'if' in temp:
				print('Replacing If')
				temp = temp.replace('{', ' then')
				toadd = toadd + temp + '\n'
			elif 'while' in temp:
				print('While Looping')
				temp = temp.replace('{', '')
				toadd = toadd + temp + ' do \n'
			elif 'function' in temp:
				print('Function Replaced')
				temp = temp.replace('{', ' ')
				toadd = toadd + temp + '\n'
			elif temp[0] == '}':
				print('Adding End')
				toadd = toadd + 'end \n'
			else:
				toadd = toadd + temp + '\n'
		else:
			toadd = toadd + ''

	f.write(toadd)
	f.close()
	print('Compiled ' + filename + ' into ' + outputfile)


main()
