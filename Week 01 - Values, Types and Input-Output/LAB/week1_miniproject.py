"""
RECORD CHECK  -  my version
===========================

Name  : Jasmitha Pujari
Lane  :  IT    
Date  : 27/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

host_name = input("Enter the hostname: ")
used_gb = float(input("Enter the used GB: "))   
total_gb = float(input("Enter the total GB: "))    

free = total_gb - used_gb    # 
percent = (used_gb / total_gb) * 100         

print("=" * 34)
print(f"  RECORD CHECK  -  {host_name}")
print("=" * 34)
print(f"Used GB:{used_gb:>10.2f}")
print(f"Total GB:{total_gb:>10.2f}")
print(f"Free GB:{free:>+10.2f}")
print(f"Percent:{percent:>10.2f}%")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
