l1=[1,2,3,4]
l2=[4,5,6,7]
l3=dict(zip(l1,l2))
print(l3)


l3 = {"name" : "jeevika" , "age" : "23" , "class" : "degree"}
l4={"school" : "aryan presidency school"}
l5= l3 | l4
print(l5)


l6=["jeevika","keerthana"]
l7={"designation": "software developer" , "salary" : 500000}
l8=dict.fromkeys(l6,l7)
print(l8)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys=["name" , "salary"]
my_list ={k: sample_dict[k] for k in keys}
print(my_list)


dict_m={'a' : 1 , 'b' :2 ,'c' : 3 , 'd': 4}
my_l = ['a','c']
for i in my_l:
    dict_m.pop(i)
    print(dict_m)


new_dict={'a' : 100 , 'b' : 200 ,'c' : 300 , 'd': 400}
if 200 in new_dict.values():
    print("present")
else:
    print("not present")


d = {'k1': 1, 'k2': 2, 'k3': 3}

d['k10'] = d.pop('k1')
print(d)


my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 3}


min_key = min(my_dict, key=my_dict.get)
print("Key with minimum value:", min_key)

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)

