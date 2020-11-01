import pandas as pd
import datetime
import utils
import analysis
from emailer import Emailer
import config

if __name__ == "__main__":
    print("Starting program")

    date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    df = utils.xlsx_to_df()
    curr_month = utils.curr_month_list(df)
    last_month = utils.last_month_list(df)

    analysis = analysis.Analysis(df)
    analysis.make_graph()

    #mail = Emailer()
    #mail.create_email()
    #mail.send_email()

    print("Report has been created and sent")
