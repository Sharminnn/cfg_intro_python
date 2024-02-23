#CFG Sales analysis project
#imports the csv library
import tkinter as tk
import csv
# #opens the sales csv through the reader function
with open('sales.csv', 'r') as csv_file:
     spreadsheet = csv.DictReader(csv_file)
     sales_list = []
 #this for loop appends the data in the csv into a list.
     for row in spreadsheet:
          no_ofsales = int(row['sales'])
          sales_list.append(no_ofsales)
     total_sales = sum(sales_list)
     average_sales = round(total_sales/len(sales_list))
     lowest_sales = min(sales_list)
     highest_sales = max(sales_list)

for i in range(1,len(sales_list)):
     # minus 1 from i to get the previous month
    previous_month = sales_list[i-1]
    current_month = sales_list[i]
    difference_month = str(round((current_month - previous_month)/previous_month * 100,1))+ '%'
    print(difference_month)

 # # import writer class from csv module
from csv import writer
# # List that we want to add as a new row
data = [
     [2019,'jan',5657,1234],
     [2019,'feb',7564,2266],
     [2019,'mar',3456,1234],
     [2019,'apr',8909,1034],
     [2019,'may',2300,2445],
     [2019,'jun',2348,223],
     [2019,'jul',8797,1236],
     [2019,'aug',6977,1765],
     [2019,'sep',4335,1999],
     [2019,'oct',7355,1711],
     [2019,'nov',8122,2333],
     [2019,'dec',3877,2555]
 ]
# #open the existing CSV file in append mode
# # Create a file object for this file.
with open('sales.csv','a') as csv_file:
     # pass this file object to csv.writer()
     # and get a writer object
    writer_object = writer(csv_file)
# add a loop that writes each of the items in the list into the csv file
    for i in data:
     # pass the list as an argument into the writerow()
        writer_object.writerow(i)

# creates the scatter graph using the following libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#read data using panda library
data_2 = pd.read_csv('sales.csv')
x = data_2['month']
y = data_2['sales']
year = data_2['year']

# creates a colour variable that distinguishes between 2018 and 2019 with red and blue
#we define the function here, but the code runs later on when the user presses a button in the GUI
def graph_output():
    color = np.where(year==2018,'red','blue')
    plt.title('Sales in 2018 and 2019')
    plt.xlabel('Months')
    plt.ylabel('Sales made £')
    plt.scatter(x,y,c=color)
#legend labels
    red = mpatches.Patch(color = 'red', label = '2018')
    blue = mpatches.Patch(color = 'blue', label = '2019')
# what to show on legend
    plt.legend(handles=[red,blue])
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
window = tk.Tk()

window.title("Sales Figures Programme")

first_line = tk.Label(window, text="Your sales analysis:")
first_line.pack(padx=30, pady=30)

total_sales_output = tk.Label(window, text="Your total sales in 2018 were: " + str(total_sales))
total_sales_output.pack(padx=30, pady=30)

average_sales_output = tk.Label(window, text="Your average sales in 2018 were: " + str(average_sales))
average_sales_output.pack(padx=30, pady=30)

highest_sales_output = tk.Label(window, text="Your highest sales in 2018 were: " + str(highest_sales))
highest_sales_output.pack(padx=30, pady=30)

lowest_sales_output = tk.Label(window, text="Your lowest sales in 2018 were: " + str(lowest_sales))
lowest_sales_output.pack(padx=30, pady=30)

graph_button = tk.Button(window, text="Display data", command = graph_output)
graph_button.pack(padx = 30, pady=30)

window.mainloop()
