list1 = []
list2 = []
list3 = []
value = 0

for i in range(0,4,1) :
    for k in range(0,5,1) :
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []
    list3.append(list2)

for i in range(0,4,1) :
    for k in range(0,5,1) :
        print("%3d" % list2[i][k], end="")

        list3.append(list2)
    for i in range(0, 4, 1):
        for k in range(0, 5, 1):
            print("%3d" % list2[i][k], end="")
        print("")