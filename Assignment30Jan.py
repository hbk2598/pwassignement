#Question 1
Marks=int(input("Enter your marks: "))

if Marks>90:
    print("Your grade is A")
    
elif (Marks>80 and Marks<=90):
    print("Your grade is B")

elif (Marks>=60 and Marks<=80):
  print("Your grade is C")

else:
  print("Your grade is D")


#Question 2

Price=int(input("Enter your price: "))

if (Price>100000):
    print("Your tax is 15%")
    
elif (Price>50000 and Price<=100000):
    print("Your tax is 10%")

elif(Price<50000):
  print("Your tax is 5%")

else:
  print("You are out of tax regime")


#Question 3

city=input("Enter your city: ")

if (city=='Delhi'):
  print("Monument in Delhi is Red Fort")

elif(city=='Agra'):
  print("Monument in Agra is TajMahal")

elif(city=='Jaipur'):
  print("Monument in Jaipur is Jal Mahal")

else:
  print("You entered incorrect city")



#Question 4
num = int(input("enter the number:"))
count = 0
while num > 10:
    num = num / 3 
    count += 1
print(count)

#Question 5

'''With the while loop we can execute a set of statements as long as a condition is true.'''
#Example


i = 1
while i < 6:
  print(i)
  i += 1


Question 6
pattern 1
rows=6
for i in range(rows):
  for j in range (0,i+1):
    print('*',end="")

  print(' ')

pattern 2
n=5;i=0
while(i<=n):
  print(" " * (n - i) +"*" * i)
  i+=1


#Question 7
i=10
while(i>0):
  print(i)
  i-=1


#Question 8
i=10
while(i>0):
  print(i)
  i-=1  




    
  





  
  
  
  




