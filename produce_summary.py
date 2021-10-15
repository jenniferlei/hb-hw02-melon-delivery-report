def melon_delivery(day, path):
    '''given day and file path for the day's deliveries, produce report in readable format'''
    # print the day
    print(f"Day {day}")
    the_file = open(path)

    # for each line in the file, strip right side white space and split data by |
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        # assign variables to each word
        melon, count, amount = words

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

# Call melon delivery function with day number and delivery report path
melon_delivery(1, "um-deliveries-20140519.txt")
melon_delivery(2, "um-deliveries-20140520.txt")
melon_delivery(3, "um-deliveries-20140521.txt")
