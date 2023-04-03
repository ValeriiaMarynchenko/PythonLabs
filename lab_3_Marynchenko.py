print("Лабораторна робота №3. Змінні. Базові операції вводу/виводу")
print("Завдання 1")
sigma=float(input("Enter Sigma value: "))
e=2.72
x=int(input("Enter X value: "))
mu=int(input("Enter M value: "))
pi=3.14
f=(1/sigma*((2*pi)**(1/2)))*((e)**((x-mu)**2)/(2*(sigma**2)))
print('f(x) =', f)
print()
print("Завдання 2")
john=3
mary=5
adam=6
print(john, mary, adam, sep=",")
totalApple=john+mary+adam
print(totalApple)
print("Загальна кількість яблук:", totalApple)
print()
print("Завдання 3")
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
print()
print("Завдання 4")

x = int(input("Enter X value: "))
y = 3*(x**3)-2*(x**2)+3**x-1
print("The ansver: ", y)
print()
print("Завдання 5")
hours = 2 #number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", hours) #printing the number of hours
print("Seconds in Hours: ", hours * seconds) # printing the number of seconds in a given number of hours

print("Завдання 6")
print()
print("input a float value for variable a here", end=" ")
a=float(input())
print("input a float value for variable b here", end=" ")
b=float(input())

print("output the result of addition here", a+b)
print("output the result of subtraction here", a - b)
print("output the result of multiplication here", a*b)
print("output the result of division here", a/b)
#print("\nThat's all, folks!")
print()
print("Завдання 7")
print("Enter value for x:", end=" ")
x = int(input())
# put your code here
y = (1/(x+(1/(x+(1/(x+1/(x+1/x)))))))
print("y =", y)
print()
print("Завдання 8")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

min_dura=dura%60
min_end=(mins+min_dura)%60

hou_dura=dura//60
hour_dura0=(mins+dura%60)//60

hour_end=(hour+hou_dura+hour_dura0)%24

print("The end of event(time): ", hour_end, ":", min_end)