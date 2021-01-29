import random
def get_rand_list(b,e,N):
    same=[]
    list1=(random.sample(range(b,e),N))
    list2=(random.sample(range(b,e),N))
    for i in list1:
        if i in list2:
            same.append(i)
    print(list1)
    print(list2)
    return same
print(get_rand_list(0,10,5))
