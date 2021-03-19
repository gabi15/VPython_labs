L1=[1,2,5,9]
L2=[1,9,3,4]
def in_both(L1,L2):
    set1=set(L1)
    set2=set(L2)
    new_set=set1&set2
    new_list=list(new_set)
    return new_list

print(in_both(L1,L2))