import math


def is_perfect_square(num):
    root = math.sqrt(num)
    if root ** 2 == num:
        return True
    else:
        return False
    #return root
       

print(is_perfect_square(9))
print(is_perfect_square(100))
print(is_perfect_square(225))
print(is_perfect_square(500))
    

