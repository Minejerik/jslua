--COMPILED USING MINEJERIK JSLUA COMPILER
local input
local money=100
local health=150
local loss
local strength=25
local food=10
local name
local drip=0
local car=false
local motorcycle=false
local clothes=false
local house=false
local version = 1.0
io.write("Time to play!\n")
io.write("What is your name?\n")
name = io.read() 
print("Hello",name,"!")
--COMPILED USING MINEJERIK JSLUA COMPILER
function main_loop()
io.write("What would you like to do?\n")
input = io.read()
if input == "work" then
	money=money+25
  print("Money =", (money))
end
if input == "eat" then
  if food>0 then
  health=health+5
  food=food-1
  print("Health =",(health))
  print("Food Left =",(food))  
  else
  print("You are out of food buy some!")
 end
end
--COMPILED USING MINEJERIK JSLUA COMPILER
if input=="fight" then
    loss=math.random(0,30)
    gain=math.random(1,strength/2)
	health=health-loss
  money=money+gain
    print("You Lost",(loss),"Health!")
    print("You Gained",(gain),"Dollars!")
    print("Health=",(health))
    print("Money =",(money))
end
if input=="info" then
print("Health=",(health))
print("Money =",(money))
print("Strength =",(strength))
print("Food Left =",(food)) 
print("Your Drippines =",(drip)) 
end
if input== "train" then
  strength=strength+5
--COMPILED USING MINEJERIK JSLUA COMPILER
  print("Strength =",(strength))
end
if input=="buy_food" then
food=food+1
money=money-5
print("Food Owned =",(food))
print("Money =",(money))
end
if input=="buy_car" then
  if money>=250 and car==false then
	car=true
  money=money-250
  drip=drip+250
  print("Car Now Owned")
        else
--COMPILED USING MINEJERIK JSLUA COMPILER
        if money<250 then
	      print( 250-money,"More Money Required!")
       end
        if car==true then
	      print("You already own a car!")
       end
end
end
if input=="buy_motorcycle" then
  if money>=250 and motorcycle==false then
	motorcycle=true
  money=money-250
  drip=drip+250
  print("Motorcycle Now Owned")
        else
        if money<250 then
	      print( 250-money,"More Money Required!")
       end
        if motorcycle==true then
--COMPILED USING MINEJERIK JSLUA COMPILER
	      print("You already own a motorcycle!")
       end
end
end
if input=="buy_clothes" then
  if money>=100 and clothes==false then
	clothes=true
  money=money-100
  drip=drip+100
  print("Clothes Now Owned")
        else
        if money<100 then
	      print( 100-money,"More Money Required!")
       end
        if clothes==true then
	      print("You already own Clothes!")
       end
end
end
--COMPILED USING MINEJERIK JSLUA COMPILER
if input=="buy_house" then
  if money>=400 and house==false then
	house=true
  money=money-400
  drip=drip+400
  print("House Now Owned")
        else
        if money<400 then
	      print( 400-money,"More Money Required!")
       end
        if house==true then
	      print("You already own a house!")
       end
end
end 
if input=="help" then
print("info - Gets your stats")
print("help - brings this up")
print("work - allows you to work")
--COMPILED USING MINEJERIK JSLUA COMPILER
print("buy_food - buy some food")
print("eat - eat the food")
print("fight - fight someone")
print("train - train to earn more money per fight")
print("buy_car - you buy a car $250")
print("buy_motorcycle - you buy a motorcycle $250")
print("buy_clothes - you buy some clothes $100")
print("buy_house -  you buy a house $400")
print("buy motorcycle/car/clothes/a house lets you get drippy enough to win")
print("Version =",(version))
end
if drip >= 1000 then
--COMPILED USING MINEJERIK JSLUA COMPILER
	print("You Win! You Became Drippy!")
  os.exit()
end
if health == 0 then
	print("You Died! You Lost All Your Health!")
  os.exit()
end
main_loop()
end
main_loop()
