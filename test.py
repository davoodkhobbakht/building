import copy

class miz :
    def __init__(self) -> None:
        self.time= 0
        self.available = True
        self.user = ''
        pass
    def is_available (self,time):
        if self.time <=  time:
            self.available = True
        else:
            self.available = False
        return self.available
    def setter(self,mytime, user):
        self.time = mytime
        self.user = user
        return

tabaghe_num = int(input())
miz_num =0
sakhtemoon = []


for i in range(1,tabaghe_num+1):
    miz_num = int(input())
    tabaghe = []
    for j in range(1,miz_num+1):
        desk = miz()
        desk.setter(0,"")
        tabaghe.append(desk)
    sakhtemoon.append(tabaghe)


cmd = input().split(" ")
temp_miz = miz()
temp_miz.setter(cmd[3],cmd[2])
print(sakhtemoon[0][0].time)

for tabaghe in sakhtemoon:
    print (tabaghe)
    for sit in tabaghe:
        if sit.available() == True:
            sit.user = temp_miz.user
            sit.time = temp_miz.time
            break
print(sakhtemoon)

            