name = (input("Enter your name"))
section = (input("Enter your section"))
prelim =float(input("Enter your prelim grade"))
midterm =float(input("Enter your midterm grade"))
finals =float(input("Enter your finals grade"))


average = (prelim + midterm + finals)


if   average >= 99 and average <= 100:
     percentage = 1.00
     print("Your GPA is 1.00")
elif average >= 96 and average <= 98:
     percentage = 1.25
     print("Your GPA is 1.25")
elif average >= 93 and average <= 95:
     percentage = 1.50
     print("Your GPA is 1.50")
elif average >= 90 and average <= 92:
     percentage = 175
     print("your GPA is 1.75")
elif average >= 87 and average <= 89:
     percentage = 2.00
     print("Yur GPA is 2.00")
elif average >= 84 and average <= 86:
     percentage = 2.25
     print("Your GPA is 2.25")
elif average >= 81 and average <= 83:
     percentage = 2.50
     print("Your GPA is 2.50")
elif average >= 78 and average <= 80:
     percentage = 2.875
     print("Your GPA is 2.75")
elif average >= 75 and average <= 77:
     percentage = 3.00
     print("Your GPA is 3.00")
elif average >= 75:
     percentage = 5.00
     print("Your GPA is 5.0")

else:
    print("Your everage grade is below the GPA scale.")
    

