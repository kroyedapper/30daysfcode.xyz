def string_test(str):
    count_low = count_upp = count_space  = 0
    for item in str:
        if (ord(item) == 32):
            count_space += 1
        elif (ord(item) >= 65 and ord(item) <= 90):
            count_upp += 1
        else:
            count_low += 1
    print("Upper case letters in the string was %s " %count_upp)
    print("Lowercase letters in the string was %s " %count_low)
    print("The total count of spaces was %s " %count_space)
    print(len(str))
string_test('The quick Brown Fox')
string_test('Brahma Bull')