# Assignment -1
# On DATA STRUCTURE

#list
lst = [10,33,"AMAN",[2,6,4,0],"sahu"]
print(lst)

#applying defualt function
lst.append('abc')           #add element at last place
print(lst)
lst.pop(1)                  #remove the element of the gven index
print(lst)                  #lst[1]=10 is removed and lst[1]="AMAN"
lst.append('sahu')
print(lst)
print("no. of 'abc' in list (lst)=",lst.count('abc'))     #count tslls no. of time elemnt is list
print("no. of 'sahu' in list (lst)=",lst.count('sahu'))
print("index of 10 =",lst.index(10))
print("index of 'sahu' =",lst.index('sahu'))                 #index() returns the lowest index in list that obj appears.
lst.insert(1,28)
print(lst)
lst.remove('sahu')
print(lst)            # remove() searches for the given 
                      #element in the list and removes the first matching element.
lst.reverse()
print(lst)           #reverse() reverses objects of list in place
lst.clear() 
print(lst)

#tuples
tup = (4,"tuple",'work',854)
print(tup)

#dictionary
dic1 = {"Name":'AMAN','Age' : 19,'language':'python'}
print(dic1)
dic2 = dic1.copy()
print('2nd dictionary i.e. copy of 1st is:',dic2)
dic1.get('name')
print(dic1.items())
print(dic1.keys())
popitem_dic1 = dic1.popitem()
print(dic1)
language = dic1.setdefault('language','python')
print('language-->',language)
print(dic1)
age = dic1.pop('Age')
print('Age = ',age)
print(dic1)