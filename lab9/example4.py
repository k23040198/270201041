def find_evens(my_list):
    count=0
    if len(my_list)==0:
        return count
    else:
        if my_list[0]%2==0:
            count=1
        return count + find_evens(my_list[1:])

my_list=[0,1,2,3,4,5,6]
print(find_evens(my_list))