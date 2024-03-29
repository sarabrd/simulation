import numpy as np

# Constants
num_tables = 3
table_sizes =   [1, 2, 3]
arrival_time =  [10, 13, 4, 5, 11, 9, 15]
groups =        [3, 2, 3, 2, 1, 1, 3]
stay_time =     [17, 15, 21, 30, 12, 25, 25]
profit =        [25, 15, 30, 17, 7, 10, 20]
current_arrival_index = 0

#states
B = [0,0,0]         #all tables are not occupied at the start
TNOW = minimum_value = 0            #start at time is 0
TNEXT = 0
Termination = 60   #to change
T_plus = Termination + 1
EC =  [T_plus, T_plus, T_plus, arrival_time[current_arrival_index], 60] #event calendar: departure1, departure2, departure3, arrival, termination

#kpis
total_profit = 0
utilization = [0,0,0]
difference = [0,0,0]

while TNOW <= Termination:
    print("---------------------")
    print(TNOW, ",",TNEXT, ",", B, ",",EC)
    minimum_value = min(EC)

    #first, departure happens
    if minimum_value in (EC[0], EC[1], EC[2]):
        print("departure at", TNOW)
        for i, b in enumerate(B):
            if minimum_value == EC[i]:
                B[i] = 0
                TNOW = EC[i]
                EC[i] = T_plus
    
    # if the next thing that happens is an arrival
    elif minimum_value == EC[3]: #and minimum_value not in (EC[0], EC[1], EC[2]):
        print("arrival at", EC[3])
        TNOW = EC[3]

        for i,table in enumerate(table_sizes):
            if table >= groups[current_arrival_index] and B[i] == 0:
                B[i] = 1
                EC[i] = EC[3] + stay_time[current_arrival_index]
                total_profit += profit[current_arrival_index]
                utilization[i] += stay_time[current_arrival_index]
                break

            #combining tables
            elif B[0] == 0 and B[1] == 0 and B[2] == 1 and groups[current_arrival_index] == 3:
                B[0] = B[1] = 1
                EC[0] = EC[1] = EC[3] + stay_time[current_arrival_index]
                total_profit += profit[current_arrival_index]

        #schedule a new arrival  
        EC[3] += arrival_time[current_arrival_index+1]  
        current_arrival_index += 1
        TNEXT = EC[3]

    else:
        print("terminantion")
        print("total profit", total_profit)

        #still remove utilization of those that haven't left yet
        for i, b in enumerate(B):
            if b == 1:
                difference[i] = EC[i] - Termination
                utilization[i] = utilization[i] - difference[i]

        utilization = np.array(utilization, dtype=float)  # Convert to floating-point type
        utilization /= Termination
        print("utilization", utilization)
        break

    


