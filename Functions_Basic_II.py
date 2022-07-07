print("***Countdown***")
arg = 5
def countdown(param):
    my_list = []
    for i in range(param,0,-1):
        my_list.append(i)
    return my_list
print(countdown(arg))

print("\n***Print and Return***")
def print_and_return(number_list):
    print(number_list[0])
    return(number_list[1])
print(print_and_return([1,2]))

print("\n***First Plus Length***")
def first_plus_length(list_in):
    return list_in[0] + len(list_in)
print(first_plus_length([1,2,3,4,5]))

print("\n***Values Greater than Second***")
def values_greater(my_list):
    if len(my_list) < 2:
        return False
    my_new_list = []
    for list in my_list:
        if list > my_list[1]:
            my_new_list.append(list)
    print(len(my_new_list))
    return my_new_list
print(values_greater([5,2,3,2,1,4]))
print(values_greater([3]))

print("\n***This Length, That Value***")
def length_value(size, val):
    my_list = []
    for i in range(0, size):
        my_list.append(val)
    return my_list
print(length_value(4,7))
print(length_value(6,2))