myList = [1,8,3,4,2,7]
print("현재 리스트 : %s " % myList)

myList.append(40)
print("append(80) 후의 리스트 " % myList)

print("pop()으로 추출한 값 ; %s " % myList.pop())
print("pop() 후의 리스트 : %s " % myList)

myList.sort()
print("sort() 후의 리스트 " % myList)

myList.reverse()
print("reverse() 후의 리스트 " % myList)

print("20값의 위치 : %d" % myList.index(2))

myList.insert(2,222)
print("insert(2,222) 후의 리스트 " % myList)

myList.remove(222)
print("remove(222) 후의 리스트 " % myList)

myList.extend([77,88,77])
print("extend([77,88,77) 후의 리스트 " % myList)

print("77값의 개수 ; %d " % myList.count(77))

