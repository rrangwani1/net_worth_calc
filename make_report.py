import pandas as pd
import datetime
import utils

if __name__ == "__main__":
    print("Starting program")

    date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    df = utils.xlsx_to_df()
    curr_month = utils.curr_month_list(df)
    last_month = utils.last_month_list(df)


    print("Report has been created and sent")
