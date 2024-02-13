weight = float(input("Enter your weight in kilograms:"))
height = float(input("Ener your height  in metres:"))
bmi = weight / (height**2)

if bmi < 18.5:
    print("you are underweight")
elif 18.5 <=bmi <25:
    category="Normal"
elif 25 <=bmi <29.9:
    category="overweight"
else:
    category="obese"
print(f"your BMI is{bmi:.2f} and your classification")