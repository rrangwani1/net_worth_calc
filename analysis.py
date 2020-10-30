'''
This module conducts analysis on the data, including
 - change in value from last month
 - creates a graph of the current available data
 - trends?
 - have a field of percentage increase, that says "you did {great, ok, bad, poor} this month" depending on percentage change
'''

import utils
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import config




class Analysis:

    def __init__(self, df):
        self.delta = 0
        self.data = df
        self.analysis_dict = dict()

    def value_change(self):
        print("value change is:{}").format(self.delta)
        return self.delta

    def make_graph(self):
        months = self.data['Month'].tolist()
        years = self.data['Year'].tolist()
        month_year = [str(months[i]) + "-" + str(years[i]) for i in range(0,len(months))]

        values = self.data['Net Worth'].apply(int).tolist()

        plt.plot(month_year, values)
        plt.xticks(rotation=70)
        plt.show()


        print("graph goes here")
