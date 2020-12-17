#!/usr/bin/env python3
import graphviz
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def run(df,target_names):
	tree = DecisionTreeClassifier()
	features = df.drop("target",axis=1).values
	target = df["target"].value

	tree.fit(features,target)

	pass  ## FIXME
