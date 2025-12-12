# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],  [200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70],  [400, 320, 110, 100],
                [550, 270, 180, 60],  [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85],  [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []

#setting outer while loop to work with rows(trips)
i = 0
while i < len(travel_costs):
    trip_expenses = []
    j = 0
    print(f"Trip {i + 1} expenses: ", end=' ') #label for the current trip

    #setting the inner while loop to work with expenses in the current trip
    while j < len(travel_costs[i]): #[i] is the trip number 1 through 12
        if travel_costs[i][j] <= 100: #check if the expense is less than 100
            trip_expenses.append('Cheap')
            print('Cheap', end=' ')
        else: 
            trip_expenses.append(travel_costs[i][j])
            print(travel_costs[i][j], end=' ')
        j += 1 #move to the next expense

        #put the append function here???
    processed_expenses.append(trip_expenses)
    print(' ') # move to the next line after each trip
    i += 1 #move to the next trip

# Testing
print('Processed Travel Expenses:', processed_expenses)