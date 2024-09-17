supercars={'lambo','bugatti','prsche','ferrari','bujji','mustang','ferrari'}

supercars.add('aston martin')
print(supercars)

result=supercars.copy()
print(result)

supercars.clear() #clear()-clear all the elements of the set and return the default value of set data type i.e. set()
print(supercars)

games1={'gta','far cry','god of war','assassins creed'}
games2={'fifa','cricket 2007','mario','gta','free fire'}
result=games1.union(games2) #union(another set)-it returns the whole element of both the sets.

result=games1.intersection(games2) #intersection(another set)- it returns the common element between both the sets.

result=games1.difference(games2)#difference(another set2)-(games1-games2) return the element which is only present in games1
result=games2.difference(games1)#difference(another set1)-(games2-games1)return the element which is only present in games2

result=games1.symmetric_difference(games2)#difference(another set2)- return the element which is present in set1&set2 by ignoring common element

fruits={'mango','strawberry','apple','pomogranate','orange','grapes'}
fruits.remove('grapes') #remove(the name of the element u want to remove)

fruits.discard('dragon fruit') #discard()-it will remove the element but if the element is not present in the set it will not give any error just like remove method
print(fruits)

junkfoodchains={'kfc','mcd','dominoes','bk','pizzahut','tacobell'}
#result=junkfoodchains.pop() #pop()-it will randomly pick one element and removes it from the set without any arguments
result=junkfoodchains.pop()
print(result)

set1={10,20,30}
set2={10,20}
#set1.update(set2) #return type none it just only update the value inside the primary set
#set1.intersection_update(set2)
#set1.difference_update(set2)
#set1.symmetric_difference_update(set2)
result=set2.issubset(set1)
#result=set1.issuperset(set2)
#result=set1.isdisjoint(set2) #disjoint-no common elements in both the set
print(result)