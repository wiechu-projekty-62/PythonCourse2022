wiersze=10
kolumny=10
for i in range(1,wiersze+1):
    for j in range(1,kolumny+1):
        il=i*j
        print("{:2d} ".format(il),end='')
    print("\n")