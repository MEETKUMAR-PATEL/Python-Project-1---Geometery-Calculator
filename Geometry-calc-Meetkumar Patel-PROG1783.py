# This is the file in which you will be saving your work on Task 1: Geometry Calculator program
# Name:                 geometry-Calc.py
# Author:               Meetkumar Patel
# Date Created:         January 24, 2022
# Date Last Modified:   January 25, 2022 

# Purpose:
#
#This will get users input for width and length for the rectangle in centimeters.
#It will then calculate the area and the perimeter of the rectangle and display it on to the console.

print("Welcome Users!!! \nThis Program Will Help You Calculate the Area and Perimeter of the rectangle.\nPlease Proceed To The Next Step")

#Take measurement from the Users.
rectangleLength = int(input("Entetr The Length Of The Rectangle In Centimeters(cm):"))

rectangleWidth = int(input("Enter The Width Of The Rectangle In Centimeters(cm):"))

#Does The calculation as per the users provided Dimensions.
area = rectangleLength * rectangleWidth

Perimeter = 2 * (rectangleLength+rectangleWidth)

print("The Area of The Rectangle is: " + str(area) + " Square Centimeters.")

print("The Perimeter of The Rectangle is: " + str(Perimeter) + " Centimeters.")

print("Thank you !!!")
