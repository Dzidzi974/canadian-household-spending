import pandas as pd

# Province code mapping
province_mapping = {
    10: 'Newfoundland and Labrador',
    11: 'Prince Edward Island',
    12: 'Nova Scotia',
    13: 'New Brunswick',
    24: 'Quebec',
    35: 'Ontario',
    46: 'Manitoba',
    47: 'Saskatchewan',
    48: 'Alberta',
    59: 'British Columbia',
    60: 'Yukon',
    61: 'Northwest Territories',
    62: 'Nunavut',
    63: 'Outside Canada'
}

# Column header mapping (from column L onward)
column_mapping = {
    'FD001': 'Food_Expenditure_Main',
    'FD003': 'Food_Expenditure_Other',
    'FD100': 'Food_Away_From_Home',
    'FD200': 'Alcoholic_Beverages',
    'FD300': 'Tobacco_Products',
    'FD400': 'Other_Food_Products',
    'FD500': 'Food_Other_1',
    'FD600': 'Food_Other_2',
    'FD700': 'Food_Other_3',
    'FD800': 'Food_Other_4',
    'TA005': 'Public_Transportation',
    'SH001': 'Shelter_Cost_Mortgage',
    'SH002': 'Shelter_Cost_Rent',
    'SH060': 'Property_Tax',
    'SH061': 'Other_Shelter_Costs',
    'HO001': 'Homeowner_Status',
    'HF001': 'Housing_Type',
    'CL030': 'Clothing_Expenditure',
    'TR001': 'Transportation_Vehicle',
    'TR002': 'Transportation_Other',
    'TR020': 'Vehicle_Purchase',
    'RE001': 'Recreation_Expenditure',
    'RE060': 'Education_Expenditure',
    'RE061': 'Other_Recreation',
    'HC001': 'Healthcare_Expenditure',
    'ED002': 'Education_Tuition',
    'CS030': 'Communication_Services',
    'ME001': 'Miscellaneous_Expenses',
    'MG001': 'Gifts_Donations',
    'TC001': 'Travel_Within_Canada',
    'TE001': 'Travel_Outside_Canada'
}

def process_survey_data(project_pumf_shs2019_flatfile_updated, sheet_name='Sheet3'):
    # Read the Excel file
    df = pd.read_excel(project_pumf_shs2019_flatfile_updated, sheet_name= 'Sheet3')
    
    # Replace province codes with names
    df['PROV'] = df['PROV'].map(province_mapping).fillna('Unknown')
    
    # Rename columns from L onward
    column_position = 11  # Column L is index 11 (0-based)
    current_columns = list(df.columns)
    
    for i in range(column_position, len(current_columns)):
        col_name = current_columns[i]
        if col_name in column_mapping:
            current_columns[i] = column_mapping[col_name]
    
    df.columns = current_columns
    
    return df

# Usage
file_path = 'project_pumf_shs2019_flatfile_updated.xlsx'
processed_df = process_survey_data(file_path)

# Save to new Excel file if needed
processed_df.to_excel('processed_survey_data.xlsx', index=False)

# Display the first few rows
print(processed_df.head())