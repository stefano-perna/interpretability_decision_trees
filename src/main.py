#!/usr/bin/env python3

import utilities as util
from decision_tree import run as dt_analysis


if __name__ == '__main__':
	df, classes = util.load_data()
	dt_analysis(df, classes)