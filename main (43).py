def is_prime(x):
    f=True
    for i in range(2, int(x**0.5+1)):
        if x%i ==0:
            f=False
    return(f)
a=int(input('Ввести число: '))
print(is_prime(a))
