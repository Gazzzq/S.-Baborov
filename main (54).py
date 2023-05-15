def schet ():
    a= int(input("введите первое число:"))
    b=int(input("введите второе число:"))
    if a>b:
        print (a-b)
    else:
        print(b-a)
    return a, b
c, d = schet()
e,f = schet ()
z, x = schet()
schet()