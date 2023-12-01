import pdfplumber 
import csv

def main():
    path_pdf = "Subsidies granted.pdf" #name of the input pdf file
    path_csv = "Subsidies granted.csv" #name of the output csv file
    number_of_pages = int(3)
    extracted_table = extract_tables(path_pdf, path_csv, number_of_pages) # calling function "extract_tables"

def extract_tables(pfd_file, csv_file, number_of_pages):
    with pdfplumber.open(pfd_file) as pdf: #opening pdf file
        result_table = [] #defining a blank list 
        # for i in range(0,len(pdf.pages)): #if you want to go through all pages in pdf
        for page in pdf.pages[0:number_of_pages]: #goinf through first 3 pages in pdf
            table = page.extract_table(table_settings = {
                "vertical_strategy": "lines", 
                "horizontal_strategy": "lines",
                }) #extracting a table from a particular page in pdf 
            rows_without_lines = [new_row(row) for row in table[1:]] #calling a function which deletes \n in one row 
            result_table.append(rows_without_lines) #writing down the modified rows into a list 
        header = new_row(table[0]) #defining the header
        csv_transfer(result_table, header, csv_file) #calling the function which creates a csv and writes down the result_table into the csv

def new_row(row_with_lines): #function which gets rid of \n
    return [i.replace("\n", " ") for i in row_with_lines] #going through rows and deleting \n


def csv_transfer(tables, header, csv_file):
    with open(csv_file, "w") as f: #opening csv file where the result will be written
        writer = csv.writer(f, delimiter = ";", lineterminator = '\n') #defining how to write tabeles from pdf into csv fil
        writer.writerow(header) #adding header to csv
        lst = [writer.writerows(i) for i in tables] #writing table rows into csv file 

if __name__ == "__main__":
    main()