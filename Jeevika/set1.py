#program 1 (add list to set)
set1={10,20,30}
list1=[40,50,60]
set1.update(list1)
print(set1)

#program 2 (Return a new set of identical items from two sets)
set2={1,2,3,4,5,6}
set3={4,5,6,7,8,9}
set4=set2.intersection(set3)
print(set4)

#program 3 (Get Only unique items from two sets)
set5={1,20,30,40,5,60}
set6={60,8,9,40,30,20}
set7=set5.symmetric_difference(set6)
print(set7)

#program 4 (update first set with items that doesn't exixts in second set
set8={1,2,3,4,5}
set9={3,4,2,8,9}
set8.difference_update(set9)
print(set8)

#program 5 (remove items from sets at once)
set10={1,2,30,40,5}
set10.clear()
print(set10)

#program 6 (Return a set of elements present in Set A or B, but not both)
setA={1,2,3,4,5}
setB={5,6,7,8,9}
setC=setA.symmetric_difference(setB)
print(setC)

#program 7(Check if two sets have any elements in common, If yes display the common elements) 
set1={1,22,3,48}
set2={22,48,55,6}
set3=set1.intersection(set2)
print(set1)


set1={1,2,3,4}
set2={2,4,5,6}
set1.symmetric_difference_update(set2)
print(set1)

set1={13,23,33,44,53}
set2={33,44,5,60,71}
set1.difference_update(set2)
print(set1)






