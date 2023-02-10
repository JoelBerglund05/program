import random


slumpa1 = random.randint(1, 6)
slumpa2 = random.randint(1, 6)
slumpa3 = random.randint(1, 6)

print(slumpa1)
print(slumpa2)
print(slumpa3)

if slumpa1 == slumpa2 == slumpa3 and slumpa1 != 6 and slumpa2 != 6 and slumpa3 != 6:
    print("du vann!")

elif slumpa2 == 6 and slumpa1 and slumpa3 == 6:
    print("Du vann storvinst!!!")

elif slumpa1 == 1 and slumpa2 == 2 and slumpa3 == 3:
    print("du vann stegvinst")
elif slumpa1 == 1 and slumpa2 == 3 and slumpa3 == 2:
    print("du vann stegvinst")
elif slumpa1 == 2 and slumpa2 == 1 and slumpa3 == 3:
    print("du vann stegvinst")
elif slumpa1 == 2 and slumpa2 == 3 and slumpa3 == 1:
    print("du vann stegvinst")
elif slumpa1 == 3 and slumpa2 == 2 and slumpa3 == 1:
    print("du vann stegvinst")
elif slumpa1 == 2 and slumpa2 == 1 and slumpa3 == 2:
    print("du vann stegvinst")

elif slumpa1 == slumpa2 or slumpa1 == slumpa3 or slumpa2 == slumpa3:
    print("du vann!")

else:
    print("du vann inte")