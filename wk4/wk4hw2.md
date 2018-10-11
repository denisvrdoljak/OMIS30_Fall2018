# OMIS 30: Week 4, HW 2


## Making a CSV Parser Function(al)

Answer the following problems in a Jupyter notebook. Submit your notebook (the .ipynb file) via Camino. 

## CSV Parser Function
Redo week 2's homework, but this time as a function. 

def simple_csv_parser(data_as_string):
“”” This function should take in a string. The string
will be csv data (rows separated by newline characters, 
values separated by commas within the rows).
The output should be a list of lists of strings. A list, of lists (each list representing 1 row) of strings (each string being 1 value
In the csv).”””



## Extra Credit
Use the sys library to create a program that reads from standard input (stdin), then uses your simple_csv_parser() function to parse the CSV. You program would be run like this from the command line:

cat some_csv_file.csv | python3 your_program.py


