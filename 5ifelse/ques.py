#leap year 
year = int(input("enter the value of year XXXX"))

if((year%4==0 and year%100!=0) or (year%400==0)):
    print(f"{year} is leap year ")
else:
    print(f"{year} is not a leap year")