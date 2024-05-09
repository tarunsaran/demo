
def add_num(num1, target):
    l1, r1 = 0, len(num1) - 1
    while l1 < r1:
        num2 = num1[l1] + num1[r1]
        if num2 == target:
            return [l1, r1]
        elif num2 < target:
            l1 += 1  # corrected
        else:
            r1 -= 1  # corrected
    return []

num2 = [2, 7, 11, 15]
target1 = 9
print(add_num(num2, target1))
nums3 = [3, 2, 4]
target2 = 6
print(add_num(nums3, target2))