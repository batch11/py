import pandas as pd

# Function to get user input and create a DataFrame
def create_dataframe():
    print("Enter data for the DataFrame:")
    
    # Number of rows and columns
    num_rows = int(input("Enter the number of rows: "))
    num_cols = int(input("Enter the number of columns: "))
    
    # Input column names
    column_names = []
    for i in range(num_cols):
        col_name = input(f"Enter the name of column {i+1}: ")
        column_names.append(col_name)
    
    # Input data row by row
    data = []
    for i in range(num_rows):
        print(f"Enter data for row {i+1}:")
        row = []
        for col_name in column_names:
            value = input(f"Enter value for {col_name}: ")
            row.append(value)
        data.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=column_names)
    return df

if __name__ == "__main__":
    df = create_dataframe()
    print("\nHere is the data you entered:")
    print(df)
