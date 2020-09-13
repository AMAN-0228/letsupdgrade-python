def matchlist(temp_lst):
    count =0
    i = 0
    I = 0
    for item in lst:
        #print(i,"len",len(temp_lst))
        for i in range(I,len(temp_lst)):
            if item == temp_lst[i]:
                count+=1
                I = i+1
                #print(i,'in ',item,I)
                #print(count)
                break
        
        #print(i,I,"now")
    if count == 3:
        print("It's a Match") 
    else:
        print("It's gone")   
   


print('comparing lists as if order is same')
lst = [1,1,5]
print('\nlist with which to be compared is',lst)
lst_comp1 =[1,5,6,4,1,2,3,5]
lst_comp2 =[1,5,6,5,1,2,3,6]
print("\ncompare 1st list",lst_comp1)
matchlist(lst_comp1)
print("\ncompare 1st list",lst_comp2)
matchlist(lst_comp2)