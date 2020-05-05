def unique(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return sorted(unique_list)

print(unique([1,1,1,5,5,5,5,8,8,1,2,3,6,9,9,4,4,4]))

print(unique([1,2,3,3,3,3,4,5]))

print(unique([1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44]))

print(unique([1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,110,20,19,34]))