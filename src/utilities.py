#!/usr/bin/env python3
import numpy as  np
import pandas as pd
from sklearn import datasets

def load_data():
	iris = datasets.load_iris()
	table = np.hstack([iris.data,iris.target.reshape((150,1))])
	iris_df = pd.DataFrame(table,
		index=None,columns=iris.feature_names + ["target"]).astype({"target":int})
	iris_class = {i:iris.target_names[i] for i in range(3)}
	return iris_df,iris_class