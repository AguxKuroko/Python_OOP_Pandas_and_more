🐍 My Python program connects to a database that I created from scratch, retrieves data, performs data processing tasks, and exports the processed data to an Excel file. It embodies a blend of object-oriented programming, utilizing classes and objects to organize related functionality, along with the implementation of functions for modular and reusable code structures.

Here's a breakdown of its functionalities:

1. **Database Connection:**
   - The program connects to a MySQL database using user-provided credentials (username, password, hostname, port, and database name).
   - It utilizes SQLAlchemy to create an engine for retrieving data from the database.

2. **Data Retrieval:**
   - It includes a class `GettingDataFromDatabase` that inherits from `ConnectionToDatabase`. This class allows users to input SQL queries to retrieve data from the connected database.

3. **Data Processing:**
   - Data types conversion: Converts data types of DataFrame to reduce memory usage.
   - Merging columns: Merges two DataFrames based on a specified column.
   - Setting index column: Sets a new index for the DataFrame.
   - Calculating ratings statistics: Computes average, maximum, and minimum values from a dataset based on grouping by a chosen column.
   - Counting subscription plans: Counts the occurrences of each subscription plan price in the provided DataFrame.

4. **Data Visualization:**
   - It includes functions to plot subscription counts using Matplotlib.

5. **Exporting Data:**
   - The program exports the processed data to an Excel file. It prompts the user to input the file name along with the file extension.

Overall, my program provides a comprehensive framework for connecting to a database, retrieving and processing data, and exporting the results to Excel. It demonstrates practical use cases of Pandas, SQLAlchemy, and Matplotlib libraries for data manipulation and visualization tasks.
