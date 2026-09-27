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

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

host_name = input("Enter the hostname: ")     # : replace with an input() call
used_gb = float(input("Enter the used GB: "))     # : replace with an input() call, converted
total_gb = float(input("Enter the total GB: "))    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

free = used_gb - total_gb    # 
percent = (used_gb / total_gb) * 100         # 


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign


print("=" * 34)
print(f"  RECORD CHECK  -  {host_name}")
print("=" * 34)
print(f"Used GB:{used_gb:>10.2f}")
print(f"Total GB:{total_gb:>10.2f}")
print(f"Free GB:{free:>+10.2f}")
print(f"Percent:{percent:>10.2f}%")

# : your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
