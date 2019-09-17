#Sign your name:Nha Tran


# 1.) Write a program that asks someone for their name and then prints their name to the screen?
Name = str(input("Hey! What's your name?"))
print(Name)

# 2. Write a  program where a user enters a base and height and you print the area of a triangle.
Base = int(input("What's the base of the triangle? "))
Height = int(input("What's the height of the triangle? "))
Area = Base * Height
print(Area)


# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = int(input("What's the radius of the circle? "))
circumference = radius * 3.14
print(circumference)

# 4. Ask a user for an integer and then print the square root.
number = int(input("Put in a number for the square root. "))
sqrt = number**.5
print(sqrt)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = int(input("What's the mass? "))
acceleration = int(input("What's the acceleration? "))
force = mass*acceleration
print("The Force is", force)
print("Get it?")


