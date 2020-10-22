'''
This module conducts analysis on the data, including
 - change in value from last month
 - creates a graph of the current available data
 - trends?
'''

import utils
import pandas as pd
import matplotlib as mpl

class Analysis:
    def __init__(self, df):
        self.delta = 0

    def value_change(self, df):
        print("value change is:{}").format(self.delta)
        return self.delta

    def make_graph(self, df):
        print("graph goes here")
