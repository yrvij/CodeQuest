def check_credit_card(credit_num):
    credit_list = [int(x) for x in str(credit_num)]
    new_credit_list = []
    for i in range(len(credit_list)):
        if i % 2 == 0:
            new_credit_list.append(credit_list[i]* 2)
            continue
        else:
            new_credit_list.append(credit_list[i])
            continue
   
    sum = 0
    for i in range(len(new_credit_list)-1):
        sum += new_credit_list[i]
        if new_credit_list[i] >= 10:
            sum -= 9
    if (sum + new_credit_list[-1]) % 10 == 0:
        return 'The credit card number is valid.'
    else:
        return 'The credit card number is invalid.'
 

credit_num = input()
print(check_credit_card(credit_num))
