import math

def Input_User(rows, cols):
    """Get matrix from user input where each element is a tuple of integers."""
    M = []
    print("Matrix Input:")
    for row_indx in range(rows):
        row = []
        for col_indx in range(cols):
            while True:
                try:
                    TS = input(f"Input triplet for position ({row_indx + 1}, {col_indx + 1}) in format (a,b,c): ")
                    # Remove surrounding parentheses and split by comma
                    triplet = tuple(map(int, TS.strip('()').split(',')))
                    if len(triplet) != 3:
                        raise ValueError
                    row.append(triplet)
                    break
                except ValueError:
                    print("Invalid format. Please enter the triplet in the format (a,b,c) with integers.")
        M.append(row)

    print("Entered Matrix:")
    for row in M:
        print(row)
    print("\n")
    return M


def cal(M):
    """Calculate the resultant triplet by taking the geometric mean across columns for each row."""
    # Resultant Matrix Initialization
    rows = len(M)
    cols = len(M[0])
    R = [[0, 0, 0] for _ in range(rows)]

    for row_idx in range(rows):
        for col_idx in range(3):
            PT = 1  # Initialize the product for this column
            for col in range(cols):
                PT *= M[row_idx][col][col_idx]  # Multiply elements

            # Calculate the geometric mean for each element in the triplet
            R[row_idx][col_idx] = round(math.pow(PT, 1 / cols), 2)

    # Print the resultant matrix
    print("Resultant Matrix:")
    for row in R:
        print(tuple(row))


def main():
    print("Enter dimensions of the matrix:")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    M = Input_User(rows, cols)
    cal(M)

if __name__ == "__main__":
    main()