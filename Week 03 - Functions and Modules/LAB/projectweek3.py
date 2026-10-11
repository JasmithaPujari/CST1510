"""
RECORD CHECK  -  my version
===========================

Name  : Jasmitha Jhagruthi Pujari
Lane  : IT      
Date  : 11/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def print_report(label,value,limit, difference, percent, status):
    print(f"Label:{label}")
    print(f"Value:{value}")
    print(f"Limit:{limit}")
    print(f"Difference:{difference}")
    print(f"Percent:{percent}")
    print(f"Status:{status}")

def status_of(value,limit):
    if value>limit:
        return"OVERLIMIT"
    else:
        return"WITHIN LIMIT"
    
def check(value,limit):
    difference=limit-value
    percent=(value/limit)*100
    return difference, percent

# ==================================================================== INPUT 
#2. Ask for your three values.

label = input("Enter the label:") 
value = float(input("Enter the value:")) 
limit = float(input("Enter the limit:"))

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
difference=limit-value  
percent = (value/limit)*100  
status = status_of(value,limit)
difference,percent=check(value,limit)

# =================================================================== OUTPUT
# 4. Print the report.
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
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
