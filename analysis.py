'''
This module conducts analysis on the data, including
 - change in value from last month
 - creates a graph of the current available data
 - trends?
 - have a field of percentage increase, that says "you did {great, ok, bad, poor} this month" depending on percentage change
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import config
from pathlib import Path




class Analysis:

    def __init__(self, df):
        self.delta = 0
        self.delta_string = ""
        self.delta_percent = 0
        self.delta_percent_string = ""
        self.performance = ""
        self.data = df
        self.analysis_dict = dict()

    def delta_calc(self):
        self.delta = self.data['Diff from last month'].iloc[-1]
        self.delta_string = '${:,.2f}'.format(self.delta)
        self.delta_percent = (self.delta)/self.data['Net Worth'].iloc[-2]
        self.delta_percent_string = "{:.2%}".format(self.delta_percent)
        self.delta_percent *= 100

        #how to do this in a clever way? like case-switch statements, or one line if statements. something clean, elegant
        if self.delta_percent < 3:
            self.performance = "Poor"
        elif self.delta_percent >= 3 and self.delta_percent < 5:
            self.performance = "Okay"
        elif self.delta_percent >= 5 and self.delta_percent < 8:
            self.performance = "Good"
        elif self.delta_percent >= 8 and self.delta_percent < 10:
            self.performance = "Great!"
        elif self.delta_percent >= 10 and self.delta_percent < 15:
            self.performance = "Really great!"
        else:
            self.performance = "Wow, really really good!!"


    def make_line_graph(self):
        Path(config.GRAPH_DIR).mkdir(parents=True, exist_ok=True)

        # Format data into lists
        months = self.data['Month'].tolist()
        years = self.data['Year'].tolist()
        month_year = [(datetime.datetime(month=int(months[i]),
                                        year=int(years[i]),
                                        day=1).strftime("%m-%Y"))
                      for i in range(0, len(months))]

        net_worth_vals = self.data['Net Worth'].apply(int).tolist()

        # Format plot y axis to be dollar values
        fig, ax = plt.subplots()
        ax.plot(month_year, net_worth_vals, marker='o')
        fmt = '${x:,.0f}'
        tick = ticker.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(tick)

        # Display y values on plot
        for i, j in zip(month_year, net_worth_vals):
            ax.annotate('${:,.2f}'.format(j), xy=(i,j-1200))

        # General plot labelling / formatting
        plt.xticks(rotation=20)
        plt.xlabel("Time (month-year)")
        plt.ylabel("Net worth ($)")
        plt.title("Net worth over time")

        plt.savefig(config.GRAPH_FILE_NAME, bbox_inches='tight')
        #plt.show()
