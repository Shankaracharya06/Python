'''
set1={1,2,3,4}
set2={2,3,6,8}
result=set1.union(set2)
print(set1)

result=set1.intersection(set2)
print(result)

result=set1.difference(set2)
print(result)

result=set1.symmetric_difference(set2)
print(result)

set1.update(set2)
print(set1)
'''
set1={1,2,3,4}
set2={2,3,4}
#set1.intersection_update(set2)
#print(set1)

#set1.difference_update(set2)
#print(set1)

set1.symmetric_difference_update(set2)
print(set1)

