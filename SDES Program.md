```python
def split(a):
    return [char for char in a]
    
def p_10(original_list):
    order_of_indices = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    shuffled_list = [original_list[i] for i in order_of_indices]
    return shuffled_list

  

def p_8(original_list):
    order_of_indices = [5, 2, 6, 3, 7, 4, 9, 8]
    selected_elements = [original_list[i] for i in order_of_indices]
    return selected_elements

  
  

def left_shift(input_list):
    first_element = input_list[0]
    shifted_list = input_list[1:] + [first_element]
    return shifted_list


def left_shift2(input_list):
    first_element = input_list[0]
    second_element = input_list[1]
    shifted_list = input_list[2:] + [first_element] + [second_element]
    return shifted_list

  
  

def keygen():
    key=input("Enter a 10 bit string:")
    key_list=split(key)
    p10=p_10(key_list)
    ls=p10[:5]
    rs=p10[5:]
    ls=left_shift(ls)
    rs=left_shift(rs)

    combined_shifts=ls+rs
    key1=p_8(combined_shifts)

    print("Key 1:",key1)
    ls2=left_shift2(ls)
    rs2=left_shift2(rs)
    combined_list_2=ls2+rs2
    key2=p_8(combined_list_2)
    print("Key 2:",key2)

keygen()
```
