def string_test(str):
    count_low = count_upp = count_symbols  = 0
    for item in str:
        if (ord(item) < 65):
            count_symbols += 1
        elif (ord(item) >= 65 and ord(item) <= 90):
            count_upp += 1
        else:
            count_low += 1
    print("Upper case letters in the string was %s " %count_upp)
    print("Lowercase letters in the string was %s " %count_low)

string_test('The quick Brown Fox')

string_test('You are a Student of 30daysofcode')


string_test('My name is Sodiq Agunbiade, I am your tutor for this cohort')

