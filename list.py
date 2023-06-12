abc = ["Raghav", "Yogi"]
print(abc)
#print(type(abc))
abc[0] = 'Yogesh'
print(abc)
#append is used when you want to add an item in the list at the ending
abc.append("Rahul")
print(abc)
#isnert is used to add the item in wherever position you want 
abc.insert(1,"Sonu")
print(abc)
law = ['ipc', 'isc']
#Extend is used to add two list together and you can add any iterable object (tuples, sets, dictionaries etc.).
abc.extend(law)
print(abc)

abc.remove('Rahul')
print(abc)
abc.pop(1)
#if you do not specify the index number in pop() so it will delete the last item from the list
print(abc)

#loop in list

for x in abc:
    print(x)