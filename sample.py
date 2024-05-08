s = input("enter sting ")
upper_case =0
lower_case = 0
for char1 in s:
    if char1.isupper():
        upper_case+=1
    elif char1.islower():
        lower_case+=1 
print("lowe_case:",lower_case)
print("upper_case:",upper_case)
#