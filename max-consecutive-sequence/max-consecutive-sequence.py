# Givne List of integers L, find the maximum Length of a sequence of
# consecutive numbers that can be formed using elements from L.
# EX: L = [1, 0, 4, 100, 2, 3, 5, 101]
#     max(len([0,1,2,3,4,5]),  len([100, 101]))
L = [1, 0, 4, 100, 2, 3, 5, 101]

def func(L):
    final_list =[]
    tmp_list=[]
    i = 0
    while(len(L) > i):
        integer = L[i]
        search_up = integer+1
        search_down = integer-1
        while search_up is not None:
            if search_up in L:
                if integer not in tmp_list:
                    tmp_list.append(integer)
                tmp_list.append(search_up)
                L.remove(search_up)
                search_up +=1
            else:
                search_up = None
        
        while search_down is not None:
            if search_down in L:
                if integer not in tmp_list:
                    tmp_list.insert(0, integer)
                tmp_list.insert(0, search_down)
                L.remove(search_down)
                search_down -=1
            else:
                search_down = None
        if len(tmp_list) > 0:
            final_list.append(tmp_list)
            tmp_list = []
        i+=1
    
    print(final_list)

    return max(len(x) for x in final_list)



print("Maximum consecutive number len:", func(L))