
# Constants
num_tables = 3
table_sizes =   [1, 2, 3]
arrival_time =  [10, 13, 4, 5, 11, 9, 15]
groups =        [3, 2, 3, 2, 1, 1, 3]
stay_time =     [17, 15, 21, 30, 12, 25, 25]
#stay_time =     [18, 15, 21, 30, 12, 25, 25]
profit =        [25, 15, 30, 17, 7, 10, 20]
current_arrival_index = 0

#states
B = [0,0,0]         #all tables are not occupied at the start
TNOW = minimum_value = 0            #start at time is 0
TNEXT = 0
Termination = 60   #to change
T_plus = Termination + 1
EC =  [T_plus, T_plus, T_plus, arrival_time[current_arrival_index], 60] #event calendar: departure1, departure2, departure3, arrival, termination

while TNOW <= Termination:
    #print("-----------------------")    
    #print("tnow [", TNOW, "]")#, "tnext [", TNEXT, "]")
    #print("b",B)
    #print("EC", EC)
    print(TNOW, ",", B, ",",EC)
    minimum_value = min(EC)
    #TNOW = minimum_value

    #first, departure happens
    # if the next thing that happens is an arrival
    if minimum_value == EC[3]: #and minimum_value not in (EC[0], EC[1], EC[2]):
        print("arrival at", EC[3])

        for i,table in enumerate(table_sizes):
            if table >= groups[current_arrival_index] and B[i] == 0:
                B[i] = 1
                EC[i] = EC[3] + stay_time[current_arrival_index]
                break
        #schedule a new arrival  
        EC[3] += arrival_time[current_arrival_index+1]  
        current_arrival_index += 1
        TNOW = EC[3]

    elif minimum_value in (EC[0], EC[1], EC[2]):
        print("departure at", TNOW)
        for i, b in enumerate(B):
            if minimum_value == EC[i]:
                b = 0
                TNOW = EC[i]
                EC[i] = T_plus
                #break

    else:
        print("terminantion")
        break

    #TNOW = TNEXT
    #TNEXT = min(EC)
    TNOW = min(EC)

    


