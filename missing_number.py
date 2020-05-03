def missing_numbers(num_list):
        start = num_list[0]
        end= num_list[-1]
        return set(range(start,end +1)).difference(num_list)

print(missing_numbers([1, 2, 3, 4, 6, 7, 10]))
print(missing_numbers([10, 11, 12, 14, 17]))
