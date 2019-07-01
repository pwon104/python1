list1 = []
list2 = []
value = 0

for i in range(0,4,1) :
    for k in range(0,5,1) :
        list1.append(value)
        value += 3
    list2.append(list1)
    list1  = []

for i in range(0,4,1) :
    for k in range(0,5,1) :
        print("%3d" % list2[i][k], end="")
    print("")