def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist


def get_element(my_list, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][pos]

def is_present(my_list,element, cmp_function):
    size = len(my_list['elements'])
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0 :
                keyexist = True
                break
        if  keyexist:
            return keypos
    return -1


def size(my_list):
    value = my_list['size']
    return value

def add_first(my_list,element):
    if len(my_list['elements']) == 0:
        my_list['elements'] = [None]
        
    if my_list['size'] >= len(my_list['elements']):
        capacidad = 2 * len(my_list['elements'])
        elements = [None] * capacidad
        for i in range(my_list['size']):
            elements[i + 1] = my_list['elements'][i]
        my_list['elements'] = elements
    else:
        for i in range(my_list['size'], 0, -1):
            my_list['elements'][i] = my_list['elements'][i - 1]
    my_list['elements'][0] = element
    my_list['size'] += 1

    return my_list

""" def add_last(my_list,element):
    if my_list['size'] == 0:
        my_list['elements'] = [None] * 1
    
    if my_list['size'] == len(my_list['elements']):  
        new_size = max(1, my_list['size'] * 2)  
        new_elements = [None] * new_size  
        
        for i in range(my_list['size']):
            new_elements[i] = my_list['elements'][i]
        
        my_list['elements'] = new_elements  

    my_list['elements'][my_list['size']] = element 
    my_list['size'] += 1 
    
    return my_list """

def add_last(my_list, element):
    if 'elements' not in my_list:
        my_list['elements'] = []
        my_list['size'] = 0
    
    my_list['elements'].append(element)
    my_list['size'] += 1

def first_element(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][0]

def last_element(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    return my_list[size(my_list)-1]

def get_element(my_list,pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][pos]

def delete_element(my_list,pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elemento = my_list['elements'][pos]
    for i in range(pos, my_list['size'] - 1):
        my_list['elements'][i] = my_list['elements'][i + 1]
    
    my_list['elements'][my_list['size'] - 1] = None
    my_list['size'] -= 1
    return my_list

def remove_first(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    elemento = my_list['elements'][0]
    for i in range(1, my_list['size']):
        my_list['elements'][i-1] = my_list['elements'][i]
    
    my_list['elements'][my_list['size'] - 1] = None
    my_list['size'] -= 1
    return elemento
    
def remove_last(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    
    elemento = my_list['elements'][my_list['size']-1]
    my_list['elements'][my_list['size']-1] = None
    my_list['size'] -= 1
    return elemento

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list['size']:
        raise IndexError('list index out of range')
    new = [None] * (my_list['size'] + 1)
    for i in range(pos):
        new[i] = my_list['elements'][i]

    new[pos] = element

    for i in range(pos, my_list['size']):
        new[i + 1] = my_list['elements'][i]

    my_list['elements'] = new
    my_list['size'] += 1

    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size'] or my_list['size'] == 0:
        raise IndexError('list index out of range')
    my_list['elements'][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 >= my_list['size'] or
        pos_2 < 0 or pos_2 >= my_list['size']):
        raise Exception('list index out of range')
    primero = pos_1
    segundo = pos_2
    my_list['elements'][pos_1] = segundo
    my_list['elements'][pos_2] = primero
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list['size']:
        raise IndexError('list index out of range')
    if pos_i + num_elements > my_list['size']:
        raise IndexError('list index out of range')
    
    sublist = {
        'elements': my_list['elements'][pos_i:pos_i + num_elements],
        'size': num_elements
    }
    return sublist

def is_empty(my_list):
    if my_list["size"] == 0 or my_list["size"] == None:
        return True
    else:
        return False
    
    
def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted    

def shell_sort(lista, sort_criteria):
    elementos = lista["elements"]
    n = lista["size"]
    gap = n // 2  

    while gap > 0:
        for i in range(gap, n):
            temp = elementos[i]
            j = i

            
            while j >= gap and sort_criteria(elementos[j - gap], temp):
                elementos[j] = elementos[j - gap]
                j -= gap
        is_sorted = True
    return is_sorted    

    
def selection_sort(my_list, default_sort_criteria):
    n = size(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if default_sort_criteria(my_list['elements'][j], my_list['elements'][min_idx]):
                min_idx = j
        my_list['elements'][i], my_list['elements'][min_idx] = my_list['elements'][min_idx], my_list['elements'][i]
    return my_list
    



# Algoritmos de ordenamiento 



def insertion_sort(my_list, sort_crit):

    elementos = my_list['elements']
    tamanio = size(my_list)
    
    for i in range(1,tamanio):
        
        el = elementos[i]
        j = i - 1
        
        while j >= 0 and sort_crit(el,elementos[j]):
            
            elementos[j+1] = elementos[j]
            j -= 1
            
        
        elementos[j+1] = el

    
    return my_list





def merge_sort(my_list, sort_crit):
    
    
    if size(my_list) > 1:
        
        mid = size(my_list) //2
        left_half = sub_list(my_list,0,mid)
        right_half = sub_list(my_list,mid,size(my_list) -mid)
        
        merge_sort(left_half, sort_crit)
        merge_sort(right_half, sort_crit)
        
        
        i = j = k = 0
        
        left_elements = left_half['elements']
        right_elements = right_half['elements']
        elements = my_list['elements']
        
        
        while i < size(left_half) and j < size(right_half):
            
            if sort_crit(left_elements[i], right_elements[j]):
                
                elements[k] = left_elements[i]
                i += 1
                
            else:
                
                elements[k] = right_elements[j]
                j += 1
                
            k += 1
            
            
        while i < size(left_half):
            
            elements[k] = left_elements[i]
            i += 1
            k += 1
            
        while j < size(right_half):
            elements[k] = right_elements[j]
            j += 1
            k += 1
            
    return my_list

def quick_sort(my_list, sort_criteria):
    if size(my_list) <= 1:
        return my_list
    
    pivot = my_list['elements'][size(my_list) - 1] 
    left = {'elements': []}
    right = {'elements': []}
    equal = {'elements': []}
    
    for element in my_list['elements']:
        if sort_criteria(element, pivot):
            left['elements'].append(element)
        elif sort_criteria(pivot, element):
            right['elements'].append(element)
        else:
            equal['elements'].append(element)
    
    sorted_left = quick_sort({'elements': left['elements']}, sort_criteria)
    sorted_right = quick_sort({'elements': right['elements']}, sort_criteria)
    
    return {'elements': sorted_left['elements'] + equal['elements'] + sorted_right['elements']}


        
        
        

    
    




