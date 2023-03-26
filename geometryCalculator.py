# Use this file to code your solution for Task 2 in Achievements.
# Name:                 geometryCalculator.py
# Author:               Meetkumar Patel
# Date Created:         January 25, 2022
# Date Last Modified:   January 30, 2022 

# Purpose:
#This program will calculate the area and perimeter of users geometrical shape ; 
# that is where users are going to select 1 shape from 3 shape from the choices given to them from the program 
#this shape are : Square , Rectangle , Circle 
# First Welcome the user
#Then ask the user which shape would they like to be calculated for
# Usage of if statements and operators
#The shapes will be numbered that is : 1 - square , 2 - Rectangle , 3-Circle.
#If the user selects 1 then ask for the side only becauase as per the properties of square all side are equal.
#Thus A=S*S AND P=S*4
#If the user selects 2 then ask for the length and width and calculate the area and perimeter 
#if the user selects 3 then ask for the radius only .

# Then complete by giving the answer and finish it by displaying it on to the console.

#while is used to create loop if the user's input is wrong.
while True:
    print("Welcome Users!!!!.\nThese program will help you calculate the area and Perimeter of Three shapes.\nPlease continue to the next step!!.")
    print("The shapes which could be calculated are as follows:\n 1-Square , 2-Rectangle , 3-Circle")

    #prompts user To choose one of the given shapes of their choice.
    num = int(input("Please Choose One Shape From The Given Choices Above:").strip(" "))  #The strip method removes all the whitespaces from the user input.

    #the user is then given again a prompt regarding the measurement as this is square so only one side of the measurement is needed.
    if num == 1:
        side = int(input("Enter One side of the square in Centimeters: "))
        area_S = side * side
        perimeter_S = side * 4
        print("The area of square is: " + str(area_S) + "Square Centimeter")
        print("The Perimeter of Square is: " + str(perimeter_S) + "Square Centimeter")
        break

    # if user selects the second option user would be asked to give two inputs thats the length and width
    #as this is a rectangle.
    elif num == 2:
        length = int(input("Enter the Length of the Rectangle in Centimeters:"))
        width = int(input("Enter the Width of the Rectangle in Centimeters: "))
        area_R = length * width
        perimeter_R = 2*(length + width)
        print("The Area of the Rectangle is: " + str(area_R) + "Square Centimeter")
        print("The Perimeter of the Rectangle is: " + str(perimeter_R) + "Centimeter.")
        break

    # if the user selects the third option then the user will be asked to give the radius of the circle.
    elif num == 3:
        pi = (22/7)
        radius = int(input("Enter the radius of the Circle in Centimeters:"))
        area_C = pi * radius ** 2
        perimeter_C = 2 * (pi * radius)
        print("The Area of Circle is : " + str(area_C) + "Square Centimeters.")
        print("The Perimeter of the circle is: " + str(perimeter_C) + "Centimeters.")
        break

    #if the user enters out of the options given the program stops.
    else:
        print("The Number You Entered is invalid\n          Please Redo!!!!!")
        

    print("            Thank you !!!")

print("Thank You !!!!")


    


