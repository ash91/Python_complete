'''
What is Matrix in Python?

These are 2D (two dimensional) data structure. In live projects and real data simulation, you have to keep the data in a sequential or tabular format. Let suppose you want to store data of three employees of three different departments. So in tabular format, it will look something like:

Employee ID	Employee Name	Employee Dept
1001A	    Ray	Technical   Head
2004B	    Karlos	        Manager
3100A	    Alex	        Lead Developer

In Python, these tables are termed as two-dimensional arrays, which are also called matrices. Python gives us the facility to represent these data in the form of lists.'''

val = [['1001A','Ray', 'Technical Head'], ['2004B', 'Karlos' , 'Manager'], ['3100A', 'Alex' , 'Lead Developer']]
print(val)

matrix = [
    [1,2,3],
    [4,5,6], 
    [7,8,9]
]
print(matrix[0:][1])