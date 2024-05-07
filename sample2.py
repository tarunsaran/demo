def square_number(number):
    list =[num**2 for num in number if num % 2 != 0]
    return list
number =[1,2,3,4,5,6,7,8,9]
print(square_number(number))