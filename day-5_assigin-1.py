
def findprime(x):
    if not x == 1:
        #print('ok')
        #i=0
        for i in range(2,x//2 +1):
            #print('ok1',' ',i,x)
            if x%i == 0:
                #print('in',i)
                return False
        else:
            #print('ook')
            return True

            

first_num = 1
last_num =2500
#lst=[]
#for i in range(1,2500):
lst = filter(findprime, range(1,2500))
print(list(lst))
