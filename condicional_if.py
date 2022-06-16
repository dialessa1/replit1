height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmc = weight / height ** 2
if bmc < 18.5:
    print('you are underweight')
elif bmc < 25:
    print('you are normal weight')
elif bmc < 30:
    print('you are slightly overweight')
else: print('you are clinically obese')
