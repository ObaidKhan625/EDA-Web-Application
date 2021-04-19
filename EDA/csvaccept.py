import os
import pandas as pd

def csv_accept():
	if os.path.exists(r'C:\Users\OBAID\OneDrive\Desktop\EDA-Simplifier\EDA\diamonds.csv'):
		df = pd.read_csv(r'C:\Users\OBAID\OneDrive\Desktop\EDA-Simplifier\EDA\diamonds.csv')
		del df[df.columns[0]]
		print(2, df.columns)
		return df