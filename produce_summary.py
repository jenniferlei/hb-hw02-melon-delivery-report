print("Day 1")
the_file = open("um-deliveries-20140519.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
