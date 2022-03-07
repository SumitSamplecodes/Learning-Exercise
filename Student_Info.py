# class containing student info
class student:
    def __init__(self,name,father_name,mother_name,roll_no):
        self.name = name
        self.father_name = father_name
        self.mother_name = mother_name
        self.roll_no = roll_no
s1 = student('ram','rampapa','rammom',1)
s2 = student('shayam','shayampop','shayammom',2)
s3 = student('rakesh','rakeshpop','rakeshmom',3)
s4 = student('kaalu','kaalupop','kaalumom',4)
s6 = student('sharan', 'sharanpop', 'sharanmom',6)
s8 = student('richa', 'richapop','richamom',8)
s5 = student('shree', 'shreepop', 'shreemom', 5)
s7 = student('rahul', 'rahulpop', 'rahulmom',7)

l1_list = []
l1_list.append(s1)
l1_list.append(s2)
l1_list.append(s3)
l1_list.append(s4)
l1_list.append(s6)
l1_list.append(s8)
l1_list.append(s5)
l1_list.append(s7)
for obj in l1_list:
    #print(obj.roll_no , obj.name , obj.mother_name , obj.father_name)
    print(obj.roll_no, ' ', obj.name, ' ', obj.mother_name, ' ', obj.father_name)

# shorting the list
print('***********************')

l2_list = sorted(l1_list, key=lambda x: getattr(x, 'roll_no'), reverse=False)

for obj1 in l2_list:
    print(obj1.roll_no,'',obj1.name,'',obj1.father_name,'',obj1.mother_name)

# deleting in the list
print('******//////////////**********')
#list_length = [len(l1_list)]
#list_middle = [len(l1_list)//2]

mid_value = lambda  x: len(x) // 2
last_index =  len(l1_list)-2
print (mid_value(l1_list),' ', last_index)
del l1_list[mid_value(l1_list)]



del l1_list[last_index]
for obj1 in l1_list:
    print(obj1.roll_no,'',obj1.name,'',obj1.father_name,'',obj1.mother_name)










