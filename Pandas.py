print("Pandas")
'''
Data Manipulation - Changing, Organizing, or preparing data to make it useful and easier to understand
To clean, transform, and structure raw data for better usability. 

Data Analysis -  Extracting patterns, trends and insights from the data to solve problems
To answer questions or identify trends using data  

Pandas is a powerful and popular python library designed  for data manipulation and data analysis
It simplifies working with structured datasets like tables, spreadsheets, or time-series data.

What makes it unique
1. Works seamlessly with structured data formats like CSV and Excel
2. Handles missing values easily
3. Built on NumPy for fast computations

Why prefer Pandas
1. Performance - Handles millions of rows efficiently
2. Ease of Use - Beginner-friendly syntax for cleaning and transforming data
3. Integrations - Works with libraries like Matplotlib(visualizations) and Scikit-learn

SERIES - It is a 1D labeled array that can hold any data type: integers, float, strings, or even Python objects.
Each elements in the Series has a unique label called an index

DATAFRAME - It is a 2D labeled data structure in Pandas, similar to a table ina database, an Excel spreadsheet, or a SQL table 
'''

import pandas as pd
# read data from a CSV file into a dataframe
df=pd.read_csv("sales_data_sample.csv",encoding="latin1")
print(df)
'''
For reading json file
ff=pd.read_json("sample_Data.json")
print(ff)
'''
info={
    "Name":['Vedaant','Siddharth','Anoop','Rajat'],
    "Age":[20,21,22,21],
    "City":['Tehri','Pauri','Tehri','Chamoli']
}
df=pd.DataFrame(info)
print(df)

# To this as a File
df.to_csv("info.csv",index=False)
df.to_json("info.json",orient="records")
df.to_excel("hello.xlsx",index=False)


'''
Data Explore

1. understand the data set
2. identify the problems
3. plan next steps

head(n) - if there is no n then default is 5
tail(n) - if there is no n then default is 5 
'''
import pandas as pd
ff=pd.read_json("sample_Data.json")
print("Display 10 rows of first")
print(ff.head(10))

print("Display 10 rows of last")
print(ff.tail(10))

'''
To nerf these problems
1.  Number of columns , rows
2. what type of data stored
3. missing value or data

info() method functions
1. Number of rows and columns
2. Columns names
3. int64 float64 objects
4. Non null counts
'''

import pandas as pd
fe=pd.read_json("sample_Data.json")
print(fe.info())

infom={
    "Name":['Vedaant','Siddharth','Anoop','Rajat'],
    "Age":[20,21,22,21],
    "City":['Tehri','Pauri','Tehri','Chamoli']
}
dcf=pd.DataFrame(infom)

print("Displaying the info of data set")
print(dcf.info())

'''
describe() - It is a powerful function used to generate a statistical summary of the DataFrame or Series, providing a quick overview 
of the data's central tendency, dispersion, and shape of distribution.
'''
import pandas as pd
lico={
     "Name":['Vedaant','Siddharth','Anoop','Rajat','Alice','Bob','Maivish'],
    "Age": [21,22,12,17,19,24,26,],
    "Salary":[5000,6000,7000,3400,9999,2000,4444],
    "Performance score":[89,99,96,83,77,91,84]
 }
hec=pd.DataFrame(lico)

print("Sample data frame")
print(hec)
print("Descriptive statistics")
print(hec.describe())