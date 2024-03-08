import pandas as pd
import matplotlib.pyplot as plt
import openpyxl  # for Excel files to read/write


def converting_data_types(data: pd.DataFrame):
    """Converts data frame data types to others, reducing memory usage."""
    print(f"Data types before conversion:\n{data.dtypes}")
    data = data.convert_dtypes()
    print(f"Data types after conversion:\n{data.dtypes}")
    while True:
        additional_conversion = input("Do you want to perform additional conversion? y/n?: ").lower()
        if additional_conversion == 'n':
            break
        data = data.astype({input("Enter the column name: "): input("Enter the new data type: ")})
    print(f"Final data types ↓\n{data.dtypes}")
    return data


def merging_columns(data1: pd.DataFrame, data2: pd.DataFrame):
    """Merge two DataFrames based on a specified column."""
    sample_data = input("Do you wish to see a sample of the data? ").lower()
    if sample_data == 'y':
        print(data1.sample(), "\n", data2.sample())
    column_name = input("Enter the column name for merging: ")
    merge = input("What kind of merge do you wish to perform - 'left', 'right', 'inner', 'outer', 'cross'? ").lower()
    after_merge = data1.merge(data2, on=column_name, how=merge)
    return after_merge


def set_index_column(data: pd.DataFrame):
    """Setting a new index by choosing a specific column"""
    data.set_index((input("Insert column name that will be set as new index: ")), inplace=True)
    return data


def calculate_ratings_stats(data: pd.DataFrame):
    """Function to get AVG, MAX, MIN values from a dataset based on grouping by a chosen column"""
    stats_df = data.groupby(input("Name of the column that grouping will be performed by: ")).agg(
        MIN=('Rating', 'min'),
        AVG=('Rating', lambda x: round(x.mean())),
        MAX=('Rating', 'max')

    ).reset_index()

    stats_df.columns = ['Anime_name', 'MIN', 'AVG', 'MAX']

    return stats_df


def count_subscription_plans(data: pd.DataFrame):
    """Counts the number of occurrences of each subscription plan price in the provided DataFrame"""
    result = data['Sub_price'].value_counts().reset_index()
    result.columns = ['Sub_price', 'Subscription_Count']

    return result


def plot_subscription_counts(data: pd.DataFrame):
    """Plot a bar chart showing the number of subscriptions by subscription price."""
    # Create a bar chart
    colors = ['green', 'yellow', 'red']
    plt.bar(data['Sub_price'], data['Subscription_Count'], color=colors)

    # Add labels and title
    plt.xlabel('Subscription Price')
    plt.ylabel('Number of Subscriptions')
    plt.title('Number of Subscriptions by Subscription Price')
    plt.show()


def export_data_to_excel(data: pd.DataFrame):
    """Exports the provided data to an Excel file."""
    while True:
        file_name = input("Insert the file name along with the file extension. For example: 'file.txt'. ")
        try:
            data.to_excel(file_name, sheet_name="Final data")
        except ValueError as e:
            print(f"Error: File '{file_name}' has an incorrect file extension. Full error message: {e}")
            continue
        else:
            print(f"Data has been exported to '{file_name}' successfully.")
            break

# xlsx
