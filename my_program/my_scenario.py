from my_program.my_class import *
from my_program.my_functions import *


def main_1():
    df = GettingDataFromDatabase()
    try_number = 3
    for x in range(3):
        try:
            data_1 = df.get_data()
            data_2 = df.get_data()
        except SelectError as se:
            print(f"SQL statement starts with 'SELECT' >>> {se}.Tries left:{try_number - 1}")
            try_number -= 1
            if try_number == 0:
                exit("You reached the limit of tries")
        else:
            merged_data = merging_columns(data_1, data_2)
            count_results = count_subscription_plans(merged_data)
            print(count_results)
            plot_subscription_counts(count_results)
            export_data_to_excel(count_results)
            break


def main_2():
    try:
        df = GettingDataFromDatabase()
        data_1 = df.get_data()
        data_2 = df.get_data()
    except SelectError as se:
        print(f"Full error : {se}")
        return
    except ValueError as ve:
        print("An error occurred while inserting credits for the login process. Full error >>>", ve)
        return
    data_1 = converting_data_types(data_1)
    merged_data = merging_columns(data_1, data_2)
    print(merged_data.sample(7))
    data_with_index = set_index_column(merged_data)
    final_data = calculate_ratings_stats(data_with_index)
    print(final_data.sort_values("MAX", ascending=False).head(5))
