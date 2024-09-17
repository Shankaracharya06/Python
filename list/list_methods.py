watches=['rolex','fastrack','fossil','titan','casio']
watches.append('sonata') 
'''append-take the element and add at the last of the list
   append will not return anything,it will return None'''

print(watches)

result=watches.copy() #copy-return the copy of the existing list
print(result)

watches.clear() #clear-clear all the elements of the list and return empty square brackets(Deafult Value of list)
print(watches)

shoes=['nike','puma','adidas','woodland','puma']
result=shoes.count('puma') #count-to count the number of item as specified as an argument
print(result)

countries=['switzerland','pakistan','india','russia','pakistan']
countries.remove('pakistan') #remove-to remove element from the list by giving the name of element as an argument
#if list has duplicated element ,it will only remove the first appearance
print(countries)

cartoons=['tom and jerry','doraemon','ninja hattori','spongebob','pink panther']
my_cartoons=['ben10','shinchan','chota bheem','motupatlu','oggy']
cartoons.append(my_cartoons) #append(what do u want to add)-add the element at end of the list result as a nested list
print(cartoons)

cartoons.extend('micky')#extend()-extend an element character by character
print(cartoons)

cartoons.insert(2,my_cartoons) #insert(position,element)-to add the element in that specified positions as a nested list
print(cartoons)

superheroes=['ironman','jai baalayya','shaktiman','black panther','deadpool']
result=superheroes.pop(0) #pop(arg/no_arg)-if no_arg by default it will take the last element(it will also remove the element from the list)

print(result)
print(superheroes)

animes=['AOT','oone piece','demons slayer','death note','DBZ']
result=animes.index('DBZ') #index(element(mandatory),starting(optional),ending(optional))- it returns the index of the specified element from the list
print(result)

supervillains=['thanos','docotor','hella','rolex','homelander','joker']
supervillains.reverse() #reverse()-it will reverse the whole element of the list(we can't reverse some specific element of the list)
print(supervillains)

bands=['1D','bts','blackpink','maroon 5','imagine dragons']
bands.sort() #sort()-it will sort according to ASCII values of the characters
print(bands)