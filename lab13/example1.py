def binary_search(list_, element):
    if len(list_) == 0:
        return -1

    else:
        mid_element = len(list_) // 2
        if element == list_[mid_element]:
            return mid_element
        elif element < list_[mid_element]:
            return binary_search(list_[0:mid_element], element)
        else:
            index= binary_search(list_[mid_element + 1:], element) 
            if index== -1 :
              pass
            else:
              index+= mid_element+1
            return index

print(binary_search([ 1,2, 5, 6, 8, 9, 74, 98, 100],3))

