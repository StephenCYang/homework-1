# PROBLEMS
#1) The total number of months included in the dataset

#2) The net total amount of "Profit/Losses" over the entire period
    #(add all values)

#3) The average of the changes in "Profit/Losses" over the entire period
    #(grab all the changes, then get the average of those)

#4) The greatest INCREASE in profits (date and amount) over the entire period
    #(grab all the INCREASES MOM and select the greatest one with its month)

#5) The greatest DECREASE in losses (date and amount) over the entire period
    #(grab all the DECREASES MOM and select the greatest one with its month)

#6) Print the analysis to the terminal and export a text file with the results.

# FINANCIAL ANALYSIS SAMPLE:
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

#-----------------------------------------------------

#IMPORTING MODULES
import os
import csv

#GRAB CVS FILE (data to be analyzed)
csv_file = os.path.join("Resources", "budget_data.csv")

#DEFINE VARIABLES (based on the HW problems)
total_months = 0 # (#1) this is used for counting the number of months from Q1
total_net_revenue = 0 # (#2) this is used as the final amount netted
# COME BACK TO THIS AND SEE IF/HOW NEEDED
net_change_revenue_list = [] #list
greatest_increase_month = "" #string
greatest_increase_amount = 0 #interger
greatest_decrease_month = "" #string
greatest_decrease_amount = 9999999999999999 #we need a really high number. probably a better way to do this, but this works.
previous_profit = 0 #interger

#Open CSV and read
with open(csv_file) as data:
    csv_reader = csv.reader(data, delimiter=",")

    #The header doesnt need to be couted during iterations, but read it and hold it aside inside of a variable.
    #After this, "next" function puts me in the next row at index 0. Next row defined below as "first_month".
    header = next(csv_reader)
    #print(f"The CSV Headers are: {header}")

    #-------------------------

    #1) Setting up to find the total number of months included in the dataset
    first_month = next(csv_reader) #I need a starting point to add/sum all months. So, I'm reading the row...
    #...where I was left off and saving it in "first_month", then function "next" moves me to the next row (index 2 or row 3).
    total_months = total_months + 1 #I'm counting the month of the row I just read above and saving it to the total...
    #... to add to it later.
   
    #2) Set up to find the total net revenue over the entire period.
    total_net_revenue += int(first_month[1]) #Here I'm grabing the net revenue value in 2nd column (index 1) and saving it...
    #... so the ForLoop can add to it at every iteration.

    previous_profit = int(first_month[1]) #There's no row/data before the first one, so I grab the net revenue value...
    #... in 2nd column (index 1) and save it as "previous_profit"
    month_of_change = [] #I'm in row 3 (or index 2) and this is the 1st month that a change can occurr. This is a list to...
    #... collect all the months in which net revenue changes occur MOM.

    #I'm in row 3 (or index 2)
    for row in csv_reader:
        #This following print is to add lines between rows for readability when printing rows
        # print("-"*50)
        # print(row)
        total_months = total_months + 1 #every iter adds 1 to the total_month counter.
        total_net_revenue += int(row[1]) #every iter adds the net revenue of that month in 2nd column (index 1) and saves it.
        
        net_change = int(row[1])-previous_profit #every iter subtracts the net revenue of that month from previous one and saves it.
        month_of_change.append(row[0]) #saves that month (index 0) at every iter.
        net_change_revenue_list.append(net_change) #saves the change in net revenue MOM to a list.
        previous_profit = int(row[1]) #sets the net revenue of that month (row) as the new "previous_profit"

        #Find the average change in net revenue by adding all the changes and dividing by number of changes.
        average_monthly_revenue_change = sum(net_change_revenue_list)/len(net_change_revenue_list)


    #Find greatest increase in net change amount with it's corresponding month.
    greatest_increase_amount = max(net_change_revenue_list)
    greatest_increase_index = net_change_revenue_list.index(greatest_increase_amount)
    greatest_increase_amount_month = month_of_change[greatest_increase_index]

    #Find greatest decrease in net change amount with it's corresponding month.
    greatest_decrease_amount = min(net_change_revenue_list)
    greatest_decrease_index = net_change_revenue_list.index(greatest_decrease_amount)
    greatest_decrease_amount_month = month_of_change[greatest_decrease_index]


    print(net_change_revenue_list)
    print(greatest_increase_amount_month,greatest_increase_amount)
    print(greatest_decrease_amount)
#PRINT ANALYSIS TO TERMINAL

analysis = (
    f"FINANCIAL ANALYSIS\n"
    f"{'-' *20}\n"
    f"Total number of months: {total_months}\n"
    f"Total of net revenue: ${total_net_revenue}\n"
    f"Average monthly change in net revenue: ${average_monthly_revenue_change}\n"
    f"Greatest increase in net revenue: {greatest_increase_amount_month} ${greatest_increase_amount}\n"
    f"Greatest decrease in net revenue: {greatest_decrease_amount_month} ${greatest_decrease_amount}\n")
print(analysis)

#EXPORT ANALYSIS TO A TXT. FILE
txt_file = os.path.join("Analysis" , "analysis.txt")

with open(txt_file , "w") as txt_file:
    txt_file.write(analysis)