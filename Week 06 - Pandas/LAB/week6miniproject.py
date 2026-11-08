"""
RECORD CHECK  -  my version
===========================

Name  : Jasmitha Pujari
Lane  : IT 
Date  : 08/11/26

Run it:   python template.py
"""
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
project_df = pd.read_csv("it_datausage.csv")#reads the data of this file i have created 

# ================================================================= PROCESS
project_df["percent"] = (project_df["used_gb"] / project_df["total_gb"]) * 100 #adding a percent column
project_df["status"] = project_df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
) #adding a status by using lamda conditon (chained condition)

# ================================================================== OUTPUT
print(project_df)#prints out the whole table
print(project_df[project_df["status"] != "OK"])#by using the boolean filter, this ony prints out the rows which are not "OK" specifically
print(project_df.groupby("status").size()) #groups the rows by status and print displaying the number of servers in each group.
project_df.to_csv("it_report.csv", index=False) #Saves project dataFrame to a new CSV file
#generating a bar chart
project_df["status"].value_counts().plot(kind="bar")
plt.title("Servers by status")
plt.savefig("it_status.png")
plt.show()

# ==========================================================================
