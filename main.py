print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
  print("You can ride the rollercoaster")
  age=int(input("What is your age? "))
  if age <= 12:
    bill=5
    print("Child tickets are $5. ")
  elif age <= 18:
    bill=7
    print("Teen tickets are $7. ")
  elif age >= 45 and age<=55:
    #Existencial crises discount
    bill=0
  else:
    bill=12
    print("Adult tickets are $12. ")

  photo_taken=input("Do you want a photo taken? Y or N ")
  if photo_taken == "Y":
    #Adds $3 to bill
    bill += 3
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you need to grow taller")
