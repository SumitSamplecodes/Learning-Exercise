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

l1_list = []
l1_list.append(s1)
l1_list.append(s2)
l1_list.append(s3)
l1_list.append(s4)
for obj in l1_list:
    #print(obj.roll_no , obj.name , obj.mother_name , obj.father_name)
    print(l1_list[1].roll_no)
