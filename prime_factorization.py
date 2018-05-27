def prime_factorization(num):
    orig_num = num
    i = 2
    factors = []
   
    while i <= orig_num:
        if (orig_num % i) == 0:
            factors.append(i)
            orig_num /= i
        else:
            i = i + 1
    product = str(num) + ' = ' + ' x '.join(str(n) for n in factors)
    return product

num = int(input('Please enter a number for its prime factorization: '))
print(prime_factorization(num))
