


print("Welcome To The UK Capitol City Game!")
print("Please Enter Your First Name to Begin!")

name = input("Please Enter Your First Name: ")

print("Greetings " + name + " Let's Begin...")

print("What Is The Capitol Of England?")

england_capitol = input("Please Enter England's Capitol City: ")

if england_capitol == "London":
    print ("The capitol of England is infact: " + england_capitol + " Well Done " + name + "!")
else:
    print("Sorry, That is Incorrect. Better Luck Next Time")


print("What Is The Capitol Of Wales?")

wales_capitol = input("Please Enter Wales's Capitol City: ")

if wales_capitol == "Cardiff":
    print ("The capitol of Wales is infact: " + wales_capitol + " Well Done " + name + "!")
else:
    print("Sorry, That is Incorrect. Better Luck Next Time")


scotland_capitol = input("Please Enter Scotland's Capitol City: ")

if scotland_capitol == "Edinburg":
    print ("The capitol of Scotland is infact: " + scotland_capitol + " Well Done " + name + "!")
else:
    print("Sorry, That is Incorrect. Better Luck Next Time")


print("What Is The Capitol Of Northen Ireland?")

nireland_capitol = input("Please Enter Northern Ireland's Capitol City: ")

if nireland_capitol == "Belfast":
    print ("The capitol of Northern Ireland is infact: " + nireland_capitol + " Well Done " + name + "!")
else:
    print("Sorry, That is Incorrect. Better Luck Next Time")

print("Thank you for playing " + name + "!" )
print("God Bless the Queen!...j/k")

    
quit()
