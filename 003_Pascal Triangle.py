#3.  🔺  Python code for PASCAL's TRIANGLE:

def printPascal(N):
    arr = [1]  # Initialize the first row
    print("Pascal's triangle with", N, "rows:")

    for i in range(N):
        print("Row", i + 1, end=" : ")

        # Print the current row
        for val in arr:
            print(val, end=" ")
        print()  # Newline after each row

        # Generate the next row
        temp = [1]  # Start the next row with 1
        for j in range(len(arr) - 1):
            temp.append(arr[j] + arr[j + 1])  # Sum of adjacent elements
        temp.append(1)  # End the row with 1
        arr = temp  # Update the current row for the next iteration


# Get user input and print Pascal's triangle
N = int(input('Enter the number of rows for Pascal\'s triangle: '))
printPascal(N)