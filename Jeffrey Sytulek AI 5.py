#Define a function to get scores and calculate the average
def get_average():
    # Ask user to input three test scores
    test1 = float(input("Enter the first test score: "))
    test2 = float(input("Enter the second test score: "))
    test3 = float(input("Enter the third test score: "))

    #Calculate average
    average = (test1 + test2 + test3) / 3

    # Return the average value to main()
    return average

#Define a function to check the average and display messages
def check_average(average):
    # Analyze the average and display a message
    if average > 95:
        print(f"Congratulations! You did great! Your average is {average:.2f}.")
    elif average >= 85 and average <= 95:
        print(f"You did great, but did not reach the best . Your average is {average:.2f}.")
    elif average >= 70 and average <= 84:
        print(f"Good effort, but you could do better. Your average is {average:.2f}.")
    else:
        print(f"You need to study harder next time. Your average is {average:.2f}.")


# Define the main function
def main():
    # Call get_average()
    average = get_average()

    # Call check_average()
    check_average(average)


# Call main()
main()


