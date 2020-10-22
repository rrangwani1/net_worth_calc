import pandas as pd

FILE_PATH = ""
FILE_NAME = "net_worth.xlsx"

def xlsx_to_df():
    df = pd.read_excel(FILE_NAME)
    return df

def curr_month_list(df):
    return df.values[-1].tolist()

def last_month_list(df):
    return df.values[-2].tolist()
