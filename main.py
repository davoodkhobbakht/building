import copy

class desk :
    duration = 0
    def __init__(self,duration,user,avail,strat_time) -> None:
        self.duration = duration
        self.user = user
        self.avail = avail
        self.start_time = strat_time
        pass
    def desk_available(self,nowtime):
        if nowtime > self.start_time+self.duration:
            self.avail = True
            return True
        else:
            self.avail = False
            return False

floor_num = range(0,int(input()))

building = []
floor = []

for i in floor_num:
    desk_num_in_each_floor = int(input())
    building.append(copy.deepcopy(floor))
    for j in range(0,desk_num_in_each_floor):
        building[i].append(desk(0,"",True,0))
do_continue = True
request_answer = []
while do_continue:
    request = input().split()
    if request[0] != "end":
        req_desk =desk(int(request[3]),request[2],False,int(request[0]))
        is_done =False
        
        for i in floor_num :
            for j in range(0,len(building[i])):
                if building[i][j].desk_available(req_desk.start_time):
                    building[i][j] = req_desk
                    is_done = True
                    request_answer.append(str.format("{0} got desk {1}-{2}",req_desk.user,i+1,j+1))
                    break
                else:
                    continue
            if is_done:
                break
        if not is_done:
            request_answer.append("no desk available")
    else:
        do_continue = False


for i in request_answer:
    print(i)
    '''print("status is:")
    for i in floor_num :
        for j in range(0,len(building[i])):
                print(str.format("floor {0} desk {1} is {2}" ,i,j,building[i][j].avail))'''
            