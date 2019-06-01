import os
import csv

# path to csv file
newbudgetpath = os.path.join("budget_data.csv")

#told python to open the csv file from path above
with open(newbudgetpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


# set variables that we will use
    months_total = 0
    net_profit = 0
    gross_change = 0
    beginning_profit = 0
    count = 0

#set list to collected new data that is going to be computed

    month_count = []
    current_profit = []
    change =  []


#Needed to iterate through the values within the csv file
    for row in csvreader:
#Asked python to find and count up all the months in the dataset
        months_total = months_total + 1

# Had python look for the month that had the greatest increase in the dataset and had it insert into the month_date list
        month_count.append(row[0])
        count = count + 1

# Had python append current_profit list by caluculating the total profit
        current_profit.append(row[1])
        net_profit = net_profit + int(row[1])

# Next I calculated the monthly change and stored it in monthly_change in order to use it to calculate the avg change

        total_profit = int(row[1])
        monthly_changes = total_profit - beginning_profit

        change.append(monthly_changes)

        gross_change = gross_change + monthly_changes
        beginning_profit = total_profit

        change_avg = (gross_change/count)
# Next, I found the biggest increase in profits and the biggest decrease in losses.
        biggest_incr = max(change)
        biggest_decr = min(change)
        inc = month_count[change.index(biggest_incr)]
        decr = month_count[change.index(biggest_decr)]


print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months:{int(months_total)}")
print(f"Total: ${str(net_profit)}")
print(f"Average Change ${str(change_avg)}")
print(f"Greatest Increase in Profits: ${str(inc ) + str( biggest_incr)}")
print(f"Greatest decrease in Profits: ${str(decr ) + str(biggest_decr)}")
