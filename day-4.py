start_num =1042000
last_num =702648265
i = 0
while True:
    temp_num = start_num + i
    temp_copy = temp_num
   
    sum = 0
    while temp_num > 0:
        a = temp_num%10
        sum += a**3
        temp_num//=10
    
    if sum == temp_copy :
        print("Armstrong number = ",temp_copy)
        break
    elif temp_copy == last_num:
        break
    else:
        pass
    i =i + 1