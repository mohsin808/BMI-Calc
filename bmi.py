print("Welcome to BMI Mass Calculator!")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"your BMI is {bmi}, you're under weight! ")
elif bmi < 25:
  print(f"your BMI is {bmi}, you're normal! ")
elif bmi < 30:
  print(f"your BMI is {bmi}, you're over weight! ")
elif bmi < 35:
  print(f"your BMI is {bmi}, you're obese! ")
else:
  print(f"your BMI is {bmi}, you're clinically obese! ")

print("#codebyMohsin!")