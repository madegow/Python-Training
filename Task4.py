
#check if individual element is same
tuple1=(1,1,1,1)
first_element=tuple1[0]
print(first_element)
for element in tuple1[1:]:
   if(element!=first_element):
    print("false")
   else:
    print("true")
    
#check all elements are same 1    
tuple2 = (1, 1, 2, 1)
first_element = tuple2[0]
print(first_element)
all_same = all(element == first_element for element in tuple2)
if all_same:
    print("true")
else:
    print("false")

#check all elements are same 2
tuple2 = (1, 1, 2, 1)
first_element = tuple2[0]
print(first_element)
if(tuple2.count(first_element)==len(tuple2)
    print("true")
else:
    print("false")
   
    
#swap two tuples 1
a= (1, 1, 1, 1)
b= (2, 2, 2, 2)
print("Before")
print(a)
print(b)
c = a
a = b
b = c
print("After")
print(a)
print(b)

#swap two tuples 2
a= (1, 1, 1, 1)
b= (2, 2, 2, 2)
print("Before")
print(a)
print(b)
a,b=b,a
print("After")
print(a)
print(b)

    

    

    
