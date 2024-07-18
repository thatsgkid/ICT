"""Part 1"""
MyValue = float(input("Enter my number: "))
YourValue = float(input("Enter your number: "))
if MyValue > YourValue:
    print("I win")
else:
    print("You win")
#Part 2
y = float(input("Enter your y-coordinate: "))
x = float(input("Enter your x-coordinate: "))
direction = input("Enter Direction 'N' 'S' 'E' or 'W' : ")
match(direction):
    case("N"):
        y+=1
    case("S"):
        y-=1
    case("E"):
        x+=1
    case("W"):
        x-=1
print(f"X coordinate is {x}")
print(f"Y coordinate is {y}")
