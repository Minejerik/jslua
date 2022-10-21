--COMPILED WITH MINEJERIK JS LUA COMPILER
print('first num?')
local num1 = io.read()
print('second num?')
local num2 = io.read()
print('operation?')
local opp = io.read()
if opp == '*' then
print(num1*num2)
else
	if opp == '/' then
	print(num1/num2)
	else
		if opp =='+' then
		print(num1+num2)
		else
			if opp =='-' then
			print(num1-num2)
			else
				print('Invalid')
			end
		end
	end
end
--COMPILED WITH MINEJERIK JS LUA COMPILER