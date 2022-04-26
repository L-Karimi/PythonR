


first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
age = input('How old are you? ')
print(age)
divisible_by_three = int(input("Enter a number:"))
if(divisible_by_three%3==0):
    print("{} is divisible by :".format(divisible_by_three))
else:
    print("{} is not divisble by :".format(divisible_by_three))
x = [100,110,120,130,140]
new_list = [m*5 for m in x]
print(new_list)
y = [[1,2],[3,4],[5,6]]
flat_list = y[0]+y[1]+y[2]
print(flat_list)
smallest = [3,6,8,2,4,1,5,7]
smallest.sort()
small = min(smallest)
print(smallest)

z = ['a','b','c','d','e','f','g','h']
xx = list(set(z))
print(xx)
divisible_by_seven = []
for num in range(100,200):
    if(num%7==0):
        divisible_by_seven.append(num)
print(divisible_by_seven)


def Rectangle(width,height):
     Area = width * height
     Perimeter = 2* (width*height)
     print(input("Area of a rectangle is : %.2f" %Area))
     print(input("Perimeter of a rectangle is : %.2f" %Perimeter))
width = float(input('Enter the with of a rectangle:'))
height = float(input('Enter the height of a rectangle:'))
Rectangle(width, height)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
if('apple' in thislist):print("Apple is here")
thislist[3] = "Blackberry"
print(thislist)
thislist[1:3] =["strawberry","currentbery"]
print(thislist)
thislist.insert(3,"Pumpkin")
print(thislist)
grceries = ["cabbages","carrots","sukums wiki","hoho"]
thislist.extend(grceries)
print(thislist)
thislist.pop(3)
print(thislist)
thislist.remove("melon")
print(thislist)
del(thislist[3])
print(thislist)
for x in thislist :
    print(thislist.pop(3))
    new_list = [x for x in thislist if 'a in x']
    print(new_list)
thislist.sort(reverse=True)
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print(grceries)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
list1.extend(list2)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
y = thisdict.values()

thisdict["registration"] = ("KBZ354K")
print(thisdict)
u = thisdict.get(3)
if 'model' in thisdict:
    print("'Yes',model is one of the characteristics of my car in the dict")