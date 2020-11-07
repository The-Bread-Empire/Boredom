import random
from time import sleep
import math
import collections
x = 1
z = 0
counting = 0
superdict = {}
superlist = []
num_list = []
print("Welcome to my bored halloween afternoon project")
sleep(2)
print("Numbers will automaticly anylize themsleves I suggest leaving it running for about 10 min before checking the stats")
sleep(1)
print("first set the settings type y for yes and n for no during the yes or no questons")
sleep(1)
print()
aa = input("Do you want it to show each try: ")
ab = input("Do you want it to show total tries: ")
ac = input("Do you want it to show total numbers counted: ")
ad = input("Do you want it to show the total average: ")
ae = input("Do you want it to show the mode: ")
aaa = input("Do you want the program to end after running a fixed amount of times: ")
if not aaa == "n":
  aa2 = input("How many times would you like it to run before stopping: ")
  aa2 = int(aa2)

print()
acount = input("please type the largest number you want the randomizer to go to: ")
acount = int(acount)
acount1 = input("please type the number you want to find: ")
acount1 = int(acount1)
print("Starting in...")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
e=0
if acount <= 0:
  acount = 100000
  print("no value was set default to 100,000")
while x == 1:
  
  randish = random.randint(1, acount)
  print(randish)
  e += 1
  num_list.insert(e, randish)
  if randish == acount1:
    z = z + 1
    x = 2
    superdict[z]=counting
    print(f"{counting + 1} numbers just checked")
    a=1
    b=0
    while a == 1:
      if b == z:
        a=3
      else:
        b += 1
        c = superdict[b]
        superlist.insert(b, c)
        if not aa == "n":
          print(f"On try {b}, {superdict[b]} numbers checked")
    d = sum(superlist)
    if not ab == "n":
      print(f"Total tries: {z}")
    if not ac == "n":
      print(f"Total: {sum(superlist)}")
    if not ad == "n":
      print(f"average: {math.floor(d/z)}")
    superlist = []
    data = collections.Counter(num_list)
    data_list = dict(data)

    # Print the items with frequency
    

    # Find the highest frequency
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(num_list):
      if not ae == "n":
        print("No mode in the list")
    else:
      #print("The Mode of the list is : " + ', '.join(map(str, mode_val)))
      g = len(mode_val)
      h = 0
      j = 0
      while not g == h:
        
        k = mode_val[h]
        l = data_list[k]
        if not ae == "n":
          print(f"mode {h + 1}: {mode_val[h]}")
        h += 1
      if not ae == "n":
        print(f"Repeated {l} times so far")
    
    sleep(15)
    x = 1
    counting = 0
  else:
    counting = counting + 1
  if not aaa == "n":
    if z == aa2:
      x = 2
      print()
      print("Program Ended")

