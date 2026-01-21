#Build a unit converter

#Now it's time to turn your attention to the second utility, converting parsecs to lightyears. One parsec is 3.26 lightyears, so you will multiply parsecs by that value to determine lightyears.

#Create a variable named `parsecs` and set it to `11`. Then add the code to perform the appropriate calculation and store the result in a variable named `lightyears`. Finally print the result on the screen with so it displays a message which resembles the following:

#**11 parsecs is ___ lightyears**

#> Remember to you can use `str` to convert numbers to strings


parsecs = 11
light_years = (parsecs * 3.26)

print("11 parsecs is " + str(light_years) + " Lightyears")