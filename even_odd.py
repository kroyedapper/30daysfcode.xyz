def even_odd(num_list):
    even_sum = odd_sum = 0
    for item in num_list:
        if item % 2 == 0:
            even_sum += 1
        else:
            odd_sum += 1
    print("Sum of even numbers is %s" % even_sum)
    print("Sum of odd numbers is %s" % odd_sum)
   
even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18])

even_odd(range(10, 35))


