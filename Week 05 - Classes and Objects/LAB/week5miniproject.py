"""
RECORD CHECK  -  my version
===========================

Name  : Jasmitha Jhagruthi Pujari
Lane  : IT   
Date  : 25/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count=0 #coutn starts from zero
    def __init__(self,label,value,limit):#stroes the label,vlaue,limit
        self.label=label
        self.value=value
        self.limit=limit

    def percent(self): #method
        return (self.value/self.limit)*100

    def status(self):
        p=self.percent()
        return "OVERLIMIT" if p>=100 else "WARNING" if p>=90 else "OK"#if its above 100 its overlimitif its above 90 warning if its other its ok
    
# ==================================================================== RECORDS

with open("fruits.txt", "w") as f:#just created a file on spot and now records the values 
    f.write("Apple,46,59\n")
    f.write("Kiwi,34,20\n")
    f.write("Cherry,102,100\n")

def load_records(path):
    records=[]
    with open(path) as f: #opens the path of the fruit 
        for line in f:
            label,value,limit=line.strip().split(",")# Removes the whitespace and separates the label, value and limit
            record=(Record(label,float(value),float(limit)))
            records.append(record)
    return records
records = load_records("fruits.txt")

# ==================================================================== OUTPUT
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Used GB  : {record.value:>20.2f}")#decimal and right aligned
    print(f"  Total GB : {record.limit:>20.2f}")
    print(f"  Status   : {record.status():>20}")
    if record.status() == "OVERLIMIT":#if its true its count the number of records which are overlimit
        Record.over_limit_count += 1
print("=" * 34)
print("Overlimit Records:",Record.over_limit_count)

# ==========================================================================

