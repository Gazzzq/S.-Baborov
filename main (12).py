line=input("").split()
cnt=0
for i,s in enumerate(line):
    if s.isdigit():
        cnt+= len(s) 
if cnt == 0:
    print("числа не обнаружены")
else:
    print("",cnt)