# Gordon Andric
# Programming
# 24 Jan 9
# CustomCounter
# Demonstrate understanding and implement main ideas from Chapter 4 including
# but not limited to for loops, string manipulation and tuples


# Welcomes the user
print("""
    Welcome to the Custom Counter App!
""")

# Create variable
choice = ""

# Continue loop until choice = no or n
while choice != "no":
    # Ask user for starting number
    start = int(input("\nYour starting number: "))
    # Ask user for ending number
    end = int(input("\nYour ending number: "))
    # Ask user for amount to count by
    countingAmount = int(input("\nHow many you want counted by: "))
    
    # Print how much the program is counting by
    print("\nCounting by", countingAmount, ":")
    
    # If the user inputs the same starting and ending number or the counting amount is equal to 0
    # print starting number
    if start == end or countingAmount == 0:
        print("Your number is", start)
    # If starting number is less than ending number and countingAmount is greater than 0
    elif start < end and countingAmount > 0:
        # Loop through the range from start to end, increasing by countingAmount
        for i in range(start, end + 1, countingAmount):  # Add 1 to end to include it in the count
            # Print each number with a space at the end
            print(i, end=" ")
    # If starting amount is greater then ending amount
    elif start > end:
        # Loop through the range from start to end, decreasing by the absolute value of countingAmount
        for i in range(start, end - 1, -abs(countingAmount)):
            # Print each number with a space at the end
            print(i, end=" ")
    # If starting amount is less than ending amount and countingAmount is less than 0 (negative)
    elif start < end and countingAmount < 0:
        # Loop through the range from start to end, decreasing by the absolute value of countingAmount
        for i in range(start, end + 1, -countingAmount):
            # Print each number with a space at the end
            print(i, end=" ")
    # Asks user if they would like to continue
    choice = input("\n\nWould you like to count again? (yes/no): ").lower()

# Greets user off of app
print("""
    Thank you for using the Custom Counter App. Goodbye!
""")

# Press the enter key to exit
input("\n\nPress the enter key to exit.\n")