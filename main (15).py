coor1=int(input("Введите координату X 1 вершины:"))
coor11=int(input("Введите координату Y 1 вершины:"))
coor2=int(input("Введите координату X 2 вершины:"))
coor22=int(input("Введите координату Y 2 вершины:"))
coor3=int(input("Введите координату X 3 вершины:"))
coor33=int(input("Введите координату Y 3 вершины:"))
perabc_first=(coor1-coor2)**2+(coor11-coor22)**2 
perabc_second=sqrt(perabc_first)
perabc_third=(coor1-coor3)**2+(coor11-coor33)
perabc_fourth=sqrt(perabc_third)
perabc_fifth=(coor2-coor3)**2+(coor22-coor33)**2
perabc_sixth=sqrt(perabc_fifth)
perabc_seveth=perabc_second+perabc_fourth+perabc_sixth
sabc_second=sabc_first/2 
print(sabc_second)
print(perabc_seveth)