# PROJECT038: Doublet and Triplet Multiplication Code

### Written by Jeffin Basil

This project performs **doublet** and **triplet** multiplication using matrices of tuples, and calculates the geometric mean across columns. It provides the option to import matrix data from an Excel file and perform operations on doublets (2-element tuples) or triplets (3-element tuples).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Features

- **Doublet Multiplication**: Process a matrix of 2-element tuples.
- **Triplet Multiplication**: Process a matrix of 3-element tuples.
- **Geometric Mean Calculation**: Computes the geometric mean across matrix columns.
- **Excel Import**: Allows importing matrix data from an Excel file.
- **User-Friendly Interface**: Includes a simple graphical interface using `Tkinter` for easier interaction.

## Installation

### Prerequisites

Ensure that Python 3.x and the following libraries are installed:

```bash
pip install pandas openpyxl tkinter
```

### Clone the Repository

```bash
gh repo clone FALLEN-01/DOUB-TRIP-LET-CALCULATOR
cd PROJECT038
```

## Usage

1. Run the main Python file to start the graphical interface:
    ```bash
    python PROJECT038_Pandas.py
    ```

2. **Select Excel File**: The program will prompt you to select an Excel file containing your matrix.

3. The program will calculate the geometric mean for each row in the matrix and display the results.


### Example Input

```text
For doublets: (2, 3), (4, 5)
For triplets: (1, 2, 3), (4, 5, 6)
```

### Example Output

```text
Resultant Matrix for Doublets:
(2.82, 3.61)
Sum of Columns: [5.64, 7.22]
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Feel free to reach out for collaboration or questions:

- **Author**: Jeffin Basil
- **Email**: jeffinbasil@gmail.com
- **GitHub**: [FALLEN-01](https://github.com/FALLEN-01)
