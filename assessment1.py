# Constants
num_tables = 3
table_sizes = [1,2,3]
arrival_time = [10, 13, 4, 5, 11, 9, 15]
groups = [3, 2, 3, 2, 1, 1, 3]
stay_time = [17, 15, 21, 30, 12, 25, 25]
#stay_time = [1, 15, 21, 30, 12, 25, 25]
profit = [25, 15, 30, 17, 7, 10, 20]

#states
last_arrival_index = 0
tables = [{'size': size, 'occupied': False, 'departure': 61} for size in table_sizes]

#event calendar
arrival = arrival_time[last_arrival_index]
TNOW = 0
departure1 = departure2 = departure3 = 61
termination = 60  

# Simulation variables
total_profit = 0
table_utilization_time = 0

while TNOW < termination:  
    
        ###DEPARTURES###
    if  min(tables[0]['departure'], tables[1]['departure'], tables[2]['departure']) <= arrival:  #should it be <= or <
        print("DEPARTURE at time", TNOW)
        min_departure = min(table['departure'] for table in tables)

        for table in tables:
            if table['departure'] == min_departure:
                table['occupied'] = False
                print("time is", TNOW,"and People left from table", table["size"])
                table['departure'] = 61


    #####ARRIVALS####
    else:
        print("ARRIVAL at time", TNOW)
        # Customer Arrival
        group_size = groups[last_arrival_index -1]
        last_arrival_index += 1

        # Finding available table
        table_found = False

        for i, table in enumerate(tables):
            if not table['occupied'] and table['size'] >= group_size:
                # Assign the group to this table
                tables[i]['occupied'] = True
                tables[i]['departure'] = TNOW + stay_time[last_arrival_index-1]
                print("the group that arrived at", arrival, "will leave at", tables[i]['departure'])


                #table_utilization[table['size']] += group_size / table['size']
                total_profit += profit[last_arrival_index - 1]
                table_found = True
                print("the group arriving has", group_size, "people and will sit at table", table['size'])
                break

            #this is the special case when the group 3 splits
            elif not tables[0]['occupied'] and not tables[1]['occupied'] and tables[2]['occupied'] and group_size == 3: 
                tables[0]['occupied'] = tables[1]['occupied'] = True
                #table_utilization[table['size']] += 0.5  # group split between tables
                total_profit += profit[last_arrival_index - 1]
                
                
                tables[0]['departure'] = TNOW + stay_time[last_arrival_index-1]
                tables[1]['departure'] = TNOW + stay_time[last_arrival_index-1]
                print("the group that arrived at", arrival, "will split and leave table 1 at", tables[0]['departure'], "and table 2 at", tables[1]['departure'],)

                table_found = True

                break
    
        arrival = TNOW + arrival_time[last_arrival_index]
        TNOW = arrival
    

print("Total profit:", total_profit)
#print("Table Utilization:", table_utilization)
