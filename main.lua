function calc() 
print('Number 1')
local num1 = io.read();
print('Number 2')
local num2 = io.read();
print('Operation')
local op = io.read();
if op == '+' then
	print(num1+num2)
	else
		if op == '-' then
			print(num1-num2)
			else
				if op == '*' then
				print(num1*num2)
				else
					if op == '/' then
					print(num1/num2)
					else
						print('INVALID OPERATION')
						calc()
end
end
end
end
end
calc()
