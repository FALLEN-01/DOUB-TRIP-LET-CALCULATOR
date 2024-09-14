'''DOCUMENTATION'''
#PROJECT038
#Doublet and Triplet mutliplication code 
#Wriiten By Jeffin Basil
#Contact : Jeffinbasil@gmail.com
#GitHub : https://github.com/FALLEN-01



import pandas as pd
import math
from tkinter import Tk, Label, Button, filedialog, messagebox, Text, END


def read_excel(file_path):
    #Excel->DataFrame
    df = pd.read_excel(file_path, sheet_name=0, header=None)
    return df


def parse_tuple(value):
    #parsing tuple
    try:
        parts = value.strip('()').split(',')
        parts = [eval(x) for x in parts]
        if len(parts) == 2 or len(parts) == 3:
            return tuple(parts)
        else:
            raise ValueError(f"Expected 2 or 3 elements, got {len(parts)}")
    except Exception as e:
        raise ValueError(f"Invalid input: {value}. Error: {e}")


def identify_Matrix(df):
    """Matrix Analyser"""
    for _, row in df.iterrows():
        for item in row:
            try:
                tuple_val = parse_tuple(str(item))
                if len(tuple_val) == 2:
                    return "doublet"
                elif len(tuple_val) == 3:
                    return "triplet"
            except ValueError as ve:
                continue
    return None


def process_doublet(df):
    #Doublet Processor
    MAT_DOUB = []
    for _, row in df.iterrows():
        try:
            MAT_DOUB.append([parse_tuple(str(x)) for x in row if len(parse_tuple(str(x))) == 2])
        except ValueError as ve:
            messagebox.showerror("Error", f"Error processing doublets: {ve}")
            return []
    return MAT_DOUB


def process_triplet(df):
    #Triplet Processor
    MAT_TRI = []
    for _, row in df.iterrows():
        try:
            MAT_TRI.append([parse_tuple(str(x)) for x in row if len(parse_tuple(str(x))) == 3])
        except ValueError as ve:
            messagebox.showerror("Error", f"Error processing triplets: {ve}")
            return []
    return MAT_TRI


def cal_doub(M_DOUB):
    #Doublet calculator
    if not M_DOUB:
        return "No valid doublet data to process."

    rows = len(M_DOUB)
    cols = len(M_DOUB[0])
    R = [[0, 0] for _ in range(rows)]

    for row_idx in range(rows):
        for col_idx in range(2):
            PT = 1
            for col in range(cols):
                PT *= M_DOUB[row_idx][col][col_idx]

            R[row_idx][col_idx] = round(math.pow(PT, 1 / cols), 2)

    result_str = "\nResultant Matrix (Doublets):\n"
    for row in R:
        result_str += str(tuple(row)) + "\n"

    col_sum_doub = [sum(row[i] for row in R) for i in range(2)]
    result_str += "\nSum of columns:\n" + str(col_sum_doub)

    return result_str


def cal_tri(M_TRI):
    #Triplet calculator
    if not M_TRI:
        return "No valid triplet data to process."

    rows = len(M_TRI)
    cols = len(M_TRI[0])
    R = [[0, 0, 0] for _ in range(rows)]

    for row_idx in range(rows):
        for col_idx in range(3):
            PT = 1
            for col in range(cols):
                PT *= M_TRI[row_idx][col][col_idx]

            R[row_idx][col_idx] = round(math.pow(PT, 1 / cols), 2)

    result_str = "\nResultant Matrix (Triplets):\n"
    for row in R:
        result_str += str(tuple(row)) + "\n"

    col_sum_trip = [sum(row[i] for row in R) for i in range(3)]
    result_str += "\nSum of columns:\n" + str(col_sum_trip)

    return result_str


class MatrixApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Matrix Doublet and Triplet Calculator")
        self.master.geometry("600x500")

        self.file_path = ""

        self.label = Label(master, text="Choose an Excel File:", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.upload_button = Button(master, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.result_text = Text(master, height=20, width=70)
        self.result_text.pack(pady=10)

        self.process_button = Button(master, text="Process Matrix", command=self.process_matrix)
        self.process_button.pack(pady=10)

    def upload_file(self):
        #Opens file dialog
        self.file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel files", "*.xlsx *.xls")])
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.file_path}")
        else:
            messagebox.showwarning("No File", "No file was selected.")

    def process_matrix(self):
        #Matrix Analyser
        if not self.file_path:
            messagebox.showwarning("No File", "Please upload a file first.")
            return

        df = read_excel(self.file_path)
        matrix_type = identify_Matrix(df)

        if matrix_type == "doublet":
            MATRIXDOUB = process_doublet(df)
            result = cal_doub(MATRIXDOUB)
        elif matrix_type == "triplet":
            MATRIXTRI = process_triplet(df)
            result = cal_tri(MATRIXTRI)
        else:
            result = "Unable to determine whether the data contains doublets or triplets."

        self.result_text.delete(1.0, END)
        self.result_text.insert(END, result)


if __name__ == "__main__":
    root = Tk()
    app = MatrixApp(root)
    root.mainloop()
