#variable
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
#department variable
deli_dept = [meat, cheese, condiment]
#if statements
if "Ham" in meat and meat[2] < 100:
    meat[2] =100
#add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
#remove and sort
deli_dept.remove(condiment)
deli_dept.sort()
#print statement
print("Initial Deli List:", deli_dept)
print("Updated Deli List:", deli_dept)



    