def sales_reports(the_file):
    '''prints sales data in a readable format from the sales report'''
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

# For day 1, open sales report and assign to the_file1 variable
# Call sales report function with the_file1 as parameter
print("Day 1")
the_file1 = open("um-deliveries-20140519.txt")
sales_reports(the_file1)

# For day 2, open sales report and assign to the_file2 variable
# Call sales report function with the_file2 as parameter
print("Day 2")
the_file2 = open("um-deliveries-20140520.txt")
sales_reports(the_file2)

# For day 3, open sales report and assign to the_file3 variable
# Call sales report function with the_file3 as parameter
print("Day 3")
the_file3 = open("um-deliveries-20140521.txt")
sales_reports(the_file3)
