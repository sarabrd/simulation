
# Constants
num_tables = 3
table_sizes =   [1, 2, 3]
arrival_time =  [10, 13, 4, 5, 11, 9, 15]
groups =        [3, 2, 3, 2, 1, 1, 3]
#stay_time =     [17, 15, 21, 30, 12, 25, 25]
stay_time =     [18, 15, 21, 30, 12, 25, 25]
profit =        [25, 15, 30, 17, 7, 10, 20]
current_arrival_index = 0

#states
B = [0,0,0]         #all tables are not occupied at the start
TNOW = 0            #start at time is 0
TNEXT = 0
Termination = 60   #to change
T_plus = Termination + 1
EC =  [T_plus, T_plus, T_plus, arrival_time[0], 68] #event calendar: departure1, departure2, departure3, arrival, termination

while TNOW < Termination:
    TNEXT = min(EC)
    Next_Type = EC.index(TNEXT)
    #update area and utilization here

    TNOW = TNEXT 

    #arrival happens
    if Next_Type == 3:
        print("arrival at", TNOW)
        for i, b in enumerate(B):
            if table_sizes[i] >= groups[current_arrival_index] and b == 0:
                b = 1
                EC[i] = TNOW + stay_time[current_arrival_index]
                break
        EC[3] = TNOW + arrival_time[current_arrival_index+1]

    #departure
    if Next_Type in [0 ,1, 2]:
        print("departure at", TNOW)
        if EC[Next_Type] == 3:#somebody is cming at the same time
            EC[i] = TNOW + stay_time[current_arrival_index+1]
        #if nobody is currently waiting 
        else:
            B[Next_Type] = 0
            EC[i] = T_plus

