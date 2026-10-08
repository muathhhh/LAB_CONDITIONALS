wi=float(input("Enter your Wieght:"))
hi=float(input("Enter your Height:"))
hi=hi/100
bmi=wi/hi**2
print("Your BMI is :",bmi)
if bmi >= 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif bmi>=18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")
