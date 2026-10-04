"""
RECORD CHECK  -  my version
===========================

Name  : Jasmitha Jhagruthi Pujari
Lane  : IT 
Date  : 04/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
while True:
    label = input("Enter the label:") #Asked for the label, make sure to always put the conditon after the wtv is given in the conditon sicne the coniton is abt label put it after label and use while True, value, limit
    if label=="quit": #the loop will not end unless you type in quit and will break the loop
        break 
    value = float(input("Enter the value:")) 
    limit = float(input("Enter the limit:"))

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.     
    difference=limit-value  
    percent = (value/limit)*100  

    if percent>=100:
        status="OVER LIMIT" #what is the status meaning if the percent is more than 100 the status shown will be overlimit likewise for over 90 otherwise OK
    elif percent>=90:
        status="WARNING"
    else:
        status="OK" # I used these three (if / elif / else)
# =================================================================== OUTPUT
# 4. Print the report.
# not sure to know the (count of how many came back OVER LIMIT and print that once, after the loop ends)
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Value:{value:>20.2f}")
    print(f"Limit:{limit:>20.2f}") 
    print(f"Difference:{difference:>+15.2f}")
    print(f"Percent:{percent:>18.2f}%")
    print(f"Status:{status:>19}")
    print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
