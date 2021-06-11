import copy

class desk :
    duration = 0
    def __init__(self,duration,user,avail) -> None:
        self.duration = duration
        self.user = user
        self.avail = avail
        pass

floor_num = range(0,int(input()))

building = []
floor = []

for i in floor_num:
    desk_num_in_each_floor = int(input())
    building.append(copy.deepcopy(floor))
    for j in range(0,desk_num_in_each_floor):
        building[i].append(desk(0,"",True))
request = input().split()
req_desk =desk(request[3],request[2],False)
is_done =False
print(building)
for i in floor_num :
    for j in range(0,len(building[i])):
        if building[i][j].avail:
            building[i][j] = req_desk
            is_done = True
            print(req_desk.user,str.format("got the floor : {0}desk:{1}",i,j))
            break
    if is_done:
        break

print("status is:")
for i in floor_num :
    for j in range(0,len(building[i])):
            print(str.format("floor {0} desk {1} is {2}" ,i,j,building[i][j].avail))
            