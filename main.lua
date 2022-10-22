--COMPILED USING MINEJERIK JSLUA COMPILER
local cmd = require('otherstuff.commands')
local work = require('otherstuff.work')
local fight= require('otherstuff.fight')
local buy = require('otherstuff.buy')
local food = require('otherstuff.food')
local sleepcount = 15
MorDays = 30
Mordayleft = 60
House = false
C = require('otherstuff.colors')
VERSION = "1.10.3"
Cycles = 0
Taxesammount = 0
math.randomseed(os.time())
local temp = math.random(1,5)
Allergie = Allergies[temp]
Energy = 150
Money = 100
RandomTemp = 0
--COMPILED USING MINEJERIK JSLUA COMPILER
print(C.red..'You are allergic to the '..Allergie.." food group"..C.none)
function MainLoop()
write(C.yellow.."What Would you like to do?\n"..C.none)
Input = string.lower(io.read())
if Input == "sleep" then
if sleepcount >= 15 then
cmd.sleep()
sleepcount = 0
else
print(C.red..'You arent tired you cant sleep!'..C.none)
end
end
if Input == "work" then
work.work()
end
if Input == "eat" then
--COMPILED USING MINEJERIK JSLUA COMPILER
food.eat()
end
if Input == "cook" then
food.cook()
end
if Input == "list_food" then
food.list()
end
if Input == "fight" then
fight.flight()
end
if Input == 'pay_rent' then
if Money>50 then
Mordayleft = Mordayleft + MorDays
print(C.green..'Paid Rent')
print('Good for another '..Mordayleft..' Cycles!'..C.none)
--COMPILED USING MINEJERIK JSLUA COMPILER
print(C.red..'You paid 50 dollars'..C.none)
Money = Money - 50
else
print(C.red.."Not Enough Money!"..C.none)
end
end
if Input == "buy_food" then
buy.food()
end
if Input == "exit" then
print("exiting!")
os.os.exit()
end
Cycles = Cycles + 1
if Mordayleft>0 then Mordayleft = Mordayleft - 1 end
--COMPILED USING MINEJERIK JSLUA COMPILER
if Cycles % 60 == 0 then
print(C.red..'You paid your taxes!')
if Money-50 > 15 then temp = math.random(15,Money-50) else temp = 5 end
if House == false then temp = temp/2 end
Taxesammount = Taxesammount +temp
print('You Paid '..temp..' Dollars'..C.none)
Money = Money - temp
end
if Money < 0 then
write('\n')
print(C.red..'Your In Debt!')
print('You Lose the game!'..C.none)
print('')
cmd.info()
os.os.exit()
end
if Mordayleft==0 then
if House == true then
--COMPILED USING MINEJERIK JSLUA COMPILER
House = false
print(C.red.."You lost your house!")
print('Taxes Cut in half and ability to cook removed!')
print('Pay Your rent for 50 dollars!'..C.none)
end
else
House = true
end
if Input == "info" then
cmd.info()
end
temp = math.random(-123123123,123123)
temp =os.time()+temp
math.randomseed(temp)
sleepcount = sleepcount +1
MainLoop()
end
MainLoop()
