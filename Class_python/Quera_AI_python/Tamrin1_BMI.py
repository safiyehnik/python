User_name = input()
password = input()
Name, Age, BMI = input().split()
Conver_BMI = "{:.3f}".format(float(BMI))
print(f'<user>\n'
f'\t<combo>{User_name}:{password}</combo>\n'
f'\t<name>{Name}</name>\n'
f'\t<age>{Age}</age>\n'
f'\t<bmi>{Conver_BMI}</bmi>\n'
f'</user>')