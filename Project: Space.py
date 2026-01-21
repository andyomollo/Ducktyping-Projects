#For this step you will be presented with the goal for the exercise, followed by an empty cell.
# Enter your Python into the cell and run it. The solution is at the bottom of the exercise.
#In the cell below, add a variable named object_size and set it to 10 to represent 10m3. 
# Then add an if statement to test if object_size is greater than 5. 
# If it is, display a message saying We need to keep an eye on this object. 
# Otherwise, display a message saying Object poses no threat.


object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print("We need to keep an eye on this object")
else:
    print("Object pose no threat")
