
#program 1 (add list to set)
set1={1,2,3}
list1=[4,5,6]
set1.update(list1)
print(set1)

#program 2 (Return a new set of identical items from two sets)
set2={1,2,3,4,5,6}
set3={4,5,6,7,8,9}
set4=set2.intersection(set3)
print(set4)

#program 3 (Get Only unique items from two sets)
set5={1,2,3,4,5,6}
set6={6,8,9,4,3,2}
set7=set5.symmetric_difference(set6)
print(set7)

#program 4 (update first set with items that doesn't exixts in second set
set8={1,2,3,4,5}
set9={3,4,2,8,9}
set8.difference_update(set9)
print(set8)

#program 5 (remove items from sets at once)
set10={1,2,3,4,5}
set10.clear()
print(set10)

#program 6 (Return a set of elements present in Set A or B, but not both)
setA={1,2,3,4,5}
setB={5,6,7,8,9}
setC=setA.symmetric_difference(setB)
print(setC)

#program 7(Check if two sets have any elements in common, If yes display the common elements) 
set1={1,2,3,4}
set2={2,4,5,6}
set3=set1.intersection(set2)
print(set1)

#program 8 (Update set1 by adding items from set2, except common items)
set1={1,2,3,4}
set2={2,4,5,6}
set1.symmetric_difference_update(set2)
print(set1)

#program 9 (Remove items from set1 that are not common to both set1 and set2)
set1={1,2,3,4,5}
set2={3,4,5,6,7}
set1.difference_update(set2)
print(set1)







