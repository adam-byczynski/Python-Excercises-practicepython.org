import datetime
current_year = int(datetime.date.today().year)

name = str(input("What's your name: "))
age = int(input("Enter your age: "))
how_many= int(input("How many times should the message be printed: "))

year_100=100-age+current_year
message=str(name+", you will be 100 years old in a year:"+str(year_100)+"\n")

print("\n"+how_many*message)

input("Press Enter to continue...")

    