
#program 1(converting 2 lists into a directory)
list1=['key1','key2','key3']
list2=['value1','value2','value3']
dict0=dict()
for i in range(0,len(list2)):
    dict0.update({list1[i]:list2[i]})
#dict0=dict(zip(list1,list2))
print(dict0)

#program 2(merge 2 dictionaries to 1)
dict1={'key1':'value1','key2':'value2'}
dict2={'key3':'value3'}
dict1.update(dict2)
print(dict1)

#Program 3 (print the value of key in nested key) 
sampleDict={'a': {'b': {'c': 'd','e': {'f':'g','h':'i'}}}}
print(sampleDict['a']['b']['e']['h'])

#program 4 (Initialize dictionary with default values)
dict1={'key4','key5'}
dict2={'key6':'value6','key7':'value7'}
result=dict.fromkeys(dict1,dict2)
print(result)

#program 5 (create dictionary by extracting keys from a given directory)
my_info = {"name": "Keertu","age": 23,"salary": 20000,"city": "Bangalore"}
keys = ["name", "salary"]
result={k:my_info[k]for k in keys}
print(result)

#program 6(delet list of keys from a directory)
my_info = {"name": "Keertu","age": 23,"salary": 20000,"city": "Bangalore"}
keys = ["name", "salary"]
for k in keys:
    my_info.pop(k)
print(my_info)


#program 7 (check if value exits)
my_info = {"name": "Keertu","age": 23,"salary": 20000,"city": "Bangalore"}
if 23  in my_info.key():
    print('23 present in a dict')

#program 8(Rename key of a dictionary)
my_info = {"name": "Keertu","age": 23,"salary": 20000,"city": "Bangalore"}
my_info['stripened'] = my_info.pop('salary')
print(my_info)


#program 9(get minimum key value)
dct1={'ke1':'100','ke2':'10','ke3':'1000'}
print(min(dct1, key=dct1.get))


#program 10 (change value of a key in nested directory)
emp_info={'ABC':{'name':'123','salary':5000},'DEF':{'name':'456','salary':10000}}
emp_info['DEF']['salary']=5000
print(emp_info)
