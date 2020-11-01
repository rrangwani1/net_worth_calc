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
        self.data = df
        self.analysis_dict = dict()
        self.fig_name = config.GRAPH_DIR + "/" + datetime.datetime.now().strftime("%m-%Y") + ".png"

    def value_change(self):
        print("value change is:{}").format(self.delta)
        return self.delta

    def make_graph(self):
        Path(config.GRAPH_DIR).mkdir(parents=True, exist_ok=True)

        months = self.data['Month'].tolist()
        years = self.data['Year'].tolist()
        month_year = [(datetime.datetime(month=int(months[i]),
                                        year=int(years[i]),
                                        day=1).strftime("%m-%Y"))
                      for i in range(0, len(months))]

        net_worth_vals = self.data['Net Worth'].apply(int).tolist()

        fig, ax = plt.subplots()
        ax.plot(month_year, net_worth_vals)
        fmt = '${x:,.0f}'
        tick = ticker.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(tick)

        plt.xticks(rotation=20)
        plt.xlabel("Time (month-year)")
        plt.ylabel("Net worth ($)")
        plt.title("Net worth over time")

        plt.savefig(self.fig_name, bbox_inches='tight')
        #plt.show()


        print("graph goes here")
