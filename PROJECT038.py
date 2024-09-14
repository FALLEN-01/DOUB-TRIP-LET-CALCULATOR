#PROJECT038
#Doublet and Triplet mutliplication code 
#Wriiten By Jeffin Basil
#Contact : Jeffinbasil@gmail.com
#GitHub : https://github.com/FALLEN-01


import math

def Input_User_Doublet(rows, cols):
    #Get matrix from user input where each element is a tuple of integers.
    M_DOUB = []
    print("\nMatrix Input :")
    for row_indx in range(rows):
        row = []
        for col_indx in range(cols):
            while True:
                try:
                    TS = input(f"Input triplet for position ({row_indx + 1}, {col_indx + 1}) in format (a,b): ")
                    doublet = tuple(map(eval, TS.strip('()').split(',')))
                    if len(doublet) != 2:
                        raise ValueError
                    row.append(doublet)
                    break
                except ValueError:
                    print("Invalid format. Please enter the triplet in the format (a,b,c) with integers.")
        M_DOUB.append(row)

    print("\nEntered Matrix:")
    for row in M_DOUB:
        print(row)
    return M_DOUB

def cal_doub(M_BOUB):
    #Calculate the resultant doublet by taking the geometric mean across columns for each row.
    # Resultant Matrix Initialization
    rows = len(M_BOUB)
    cols = len(M_BOUB[0])
    R = [[0, 0] for _ in range(rows)]

    for row_idx in range(rows):
        for col_idx in range(2):
            PT = 1
            for col in range(cols):
                PT *= M_BOUB[row_idx][col][col_idx]  # Multiply elements

            # Calculate the geometric mean for each element in the doublet
            R[row_idx][col_idx] = round(math.pow(PT, 1 / cols), 2)

    # Print the resultant matrix
    print("\nResultant Matrix:")
    for row in R:
        print(tuple(row))
    col_sum_doub = [0] * len(R[0])
    for row in R:
        for i in range(len(row)):
            col_sum_doub[i] += row[i]
    print("\nSum of columns :\n",col_sum_doub)
    while(input("Do you want to multipy the sum of column(Y/N) :")=='y'):
        MT=[1,1]
        MT[0]=int(input("\nEnter Value for position (1,1): "))
        MT[1]=int(input("Enter Value for position (1,2): "))
        col_sum_doub[0]*=MT[0]
        col_sum_doub[1]*=MT[1]
        print("\n",col_sum_doub)

def Input_User_Triplet(rows, cols):
    #Get matrix from user input where each element is a tuple of integers.
    M_TRI = []
    print("\nMatrix Input:")
    for row_indx in range(rows):
        row = []
        for col_indx in range(cols):
            while True:
                try:
                    TS = input(f"Input triplet for position ({row_indx + 1}, {col_indx + 1}) in format (a,b,c): ")
                    # Remove surrounding parentheses and split by comma
                    triplet = tuple(map(eval, TS.strip('()').split(',')))
                    if len(triplet) != 3:
                        raise ValueError
                    row.append(triplet)
                    break
                except ValueError:
                    print("Invalid format. Please enter the triplet in the format (a,b,c) with integers.")
        M_TRI.append(row)

    print("\nEntered Matrix:")
    for row in M_TRI:
        print(row)
    return M_TRI


def cal_tri(M_TRI):
    #Calculate the resultant triplet by taking the geometric mean across columns for each row.
    # Resultant Matrix Initialization
    rows = len(M_TRI)
    cols = len(M_TRI[0])
    R = [[0, 0, 0] for _ in range(rows)]

    for row_idx in range(rows):
        for col_idx in range(3):
            PT = 1  # Initialize the product for this column
            for col in range(cols):
                PT *= M_TRI[row_idx][col][col_idx]  # Multiply elements

            # Calculate the geometric mean for each element in the triplet
            R[row_idx][col_idx] = round(math.pow(PT, 1 / cols), 2)

    # Print the resultant matrix
    print("\nResultant Matrix:")
    for row in R:
        print(tuple(row))
    col_sum_trip = [0] * len(R[0])
    for row in R:
        for i in range(len(row)):
            col_sum_trip[i] += row[i]
    print("\nSum of columns :\n",col_sum_trip)

    while(input("Do you want to multipy the sum of column(Y/N) :")=='y'):
        MT=[1,1,1]
        MT[0]=int(input("\nEnter Value for position (1,1):"))
        MT[1]=int(input("Enter Value for position (1,2):"))
        MT[2]=int(input("Enter Value for position (1,3):"))
        col_sum_trip[0]*=MT[0]
        col_sum_trip[1]*=MT[1]
        col_sum_trip[2]*=MT[2]
        print("\n",col_sum_trip)


def main():

    while True:

        print("Menu\n1.Doublet\n2.Triplet")
        ch=eval(input("Enter Choice :"))
        if ch==1:
            print("Doublet\nEnter dimensions of the matrix:")
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            M_DOUB = Input_User_Doublet(rows, cols)
            cal_doub(M_DOUB)
            
        elif ch==2:
            print("Enter dimensions of the matrix:")
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            M_TRI = Input_User_Triplet(rows, cols)
            cal_tri(M_TRI)
        
        else:
            print("Ivalid Input")

        ch=input("\nDo you want to calculate matrices ? (Y/N)")
        if ch=="n" or ch=="N":
            break


if __name__ == "__main__":
    main()