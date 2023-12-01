This Python script extracts tables from a PDF file using the pdfplumber library and saves the extracted data into a CSV file. The program is designed to work with a specific PDF file containing information about granted subsidies. The extracted tables are cleaned, removing unnecessary line breaks ("\n"), and then saved into a CSV file.

# 1. Prerequisites:
Python 3.x
Install the required libraries using:

`pip install pdfplumber`

# 2. Usage
- Replace the *path_pdf* variable with the path to your input PDF file.
- Set the desired output CSV file path using the *path_csv* variable.
- Set the desired number of pages of your input PDF file by changing *number_of_pages* variable. 
- Run the script.

```python
import pdfplumber
import csv

def main():
    path_pdf = "Subsidies_granted.pdf"  # Replace with the path to your input PDF file
    path_csv = "Subsidies_granted.csv"  # Set the desired output CSV file path
    number_of_pages = int(3)
    extracted_table = extract_tables(path_pdf, path_csv, number_of_pages)  # Calling function "extract_tables"
```

Rest of the code remains unchanged

# 3. Functionality
1. The **extract_tables** function iterates through the desired number of pages pages of the PDF file and extracts tables using specified strategies for handling vertical and horizontal lines.
2. The **new_row** function removes line breaks ("\n") from each row of the table.
3. The **csv_transfer** function writes the cleaned table data, along with the header, to a CSV file using a semicolon (";") as the delimiter.

# 4. Running the Script
Execute the script by running the following command in your terminal or command prompt:

`python your_script_name.py`

Replace **your_script_name.py** with the name of the file containing the provided code.

The script will process the specified PDF file, extract tables, clean the data, and save it in the specified CSV file.
