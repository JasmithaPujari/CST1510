"""
RECORD CHECK  -  my version
===========================

Name  : Jasmitha Jhagruthi Pujari
Lane  :  IT   
Date  : 18/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
#creating a function over here

def check_record(value,limit): #check calculates the defernce and percentage between value and limit
    difference=limit-value
    percentage=(value/limit)*100
    if value>limit:
            status="OVERLIMIT"
    else:
            status="WITHIN LIMIT"
    return difference, percentage, status

def print_record(label,value,limit, difference, percentage, status): 
    print(f"Label:{label}")
    print(f"Value:{value}")
    print(f"Limit:{limit}")
    print(f"Difference:{difference}")
    print(f"Percentage:{percentage}")
    print(f"Status:{status}")

# ====================================================================== STORE
def schoolrecords(path): #creates an empty list
    records=[]
    with open(path,"r") as f:
       for line in f:
            label,value,limit=line.strip().split(",")#strip removes all the whitespaces in the beginning and the at the end and split basicall gives a whole new line after teh comma
            
            records.append({
                    "label":label,
                    "value":float(value),
                    "limit":float(limit)})
    return records
records=schoolrecords("Week 04 - Lists, Dictionaries and Files/LAB/recordprojects.txt")

      

# =============================================================== PROCESS + OUTPUT
overlimits=0 #why?0 to create a counter so the count starts from 0
with open("resultprojects.txt","w") as f:
      for record in records:
            label=record["label"]
            value=record["value"]
            limit=record["limit"]
            difference, percentage,status=check_record(value,limit)#calls the fuctions and gives it two inputs
            print_record(label,value,limit,difference,percentage,status)
            
            f.write(record["label"] + "," + status + "\n")

            if status=="OVERLIMIT":
                overlimits += 1
print("Overlimit Count:",overlimits)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
