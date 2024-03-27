import os

import pandas as pd


def read_excel_sheet(sheet_name):
    current_file_path = os.path.abspath(__file__)
    project_dir = os.path.dirname(os.path.dirname(current_file_path))
    test_data_excel_file_path = os.path.join(project_dir, 'TestData', 'Appium_Test.xlsx')

    print(f'dir = {test_data_excel_file_path}')
    try:
        # Read the Excel file
        excel_data = pd.read_excel(test_data_excel_file_path, sheet_name=sheet_name)
        # Get the column names (first row of the sheet)
        column_names = list(excel_data.columns)
        # Convert each row into a dictionary with keys as column names
        rows_as_dicts = []
        for _, row in excel_data.iterrows():
            row_dict = {column_names[i]: row[i] for i in range(len(column_names))}
            rows_as_dicts.append(row_dict)
        return rows_as_dicts
    except Exception as e:
        print("An error occurred:", e)
        return None


def get_specific_row(sheet_name, identifier_value, identifier_column='test_id' ):
    current_file_path = os.path.abspath(__file__)
    project_dir = os.path.dirname(os.path.dirname(current_file_path))
    test_data_excel_file_path = os.path.join(project_dir, 'TestData', 'Appium_Test.xlsx')

    print(f'dir = {test_data_excel_file_path}')
    try:
        # Read the Excel file
        excel_data = pd.read_excel(test_data_excel_file_path, sheet_name=sheet_name)
        # Find the row with the specified identifier value in the identifier column
        specific_row = excel_data.loc[excel_data[identifier_column] == identifier_value].to_dict(orient='records')
        return specific_row[0] if specific_row else None
    except Exception as e:
        print("An error occurred:", e)
        return None


# Example usage:
print(read_excel_sheet("RewardTest"))
print(get_specific_row("RewardTest", 'bulk_redemption'))

