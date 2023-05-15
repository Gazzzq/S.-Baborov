def schet ():
    a= int(input("введите первое число:"))
    b=int(input("введите второе число:"))
    c= int(input("введите третье число"))
    if a>b:
        print (a-b)
    elif c> b:
        print (c-b)
    else:
        print(b-a)
    return a, b, c
k, d, j = schet()
e,f,s = schet ()
z, x, w = schet()

def hai ():
    a= int(input("введите первое число:"))
    b=int(input("введите второе число:"))
    if a>b:
        print (a-b)
    else:
        print(b-a)
    return a, b
k, d = hai()
e,f = hai ()
z, x = hai()