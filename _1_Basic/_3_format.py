import datetime

name=input("enter your name: ");
dob = int(input("enter your date of birth: "));
age = datetime.datetime.now().year - dob;
print("Mr ",name,", ","your age is ",age);
print("Mr %s, you are %s years old"%(name,age))
print("Mr {}, you are {} years old".format(name,age))
print("Mr {0}, you are {1} years old,mr {0}".format(name,age))
print("Mr {myname}, you are {myage} years old, mr {myname}".format(myname=name,myage=age))
print("Mr {:4}, you are {:5} years old".format(name,age))
print(f"Mr {name}, you are {age} year old")


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


start=int(input("Enter the start value: "));
end=int(input("Enter the end value: "));
print("{0:3} {1:4} {2:5}".format("n","n^(2)","n^(3)"))
for x in range(start, (end+1)):# for range does not always include the last value
   print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

table = {'tony': 1980, 'sylvester': 1973, 'ebere': 1983}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))



