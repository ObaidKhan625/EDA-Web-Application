import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = [1,1, 2, 3, 2, 4, 5, 3, 4, 2, 1, 2, 4, 3, 2]

try:
	sns.histplot(x = x, discrete=False, element='poly', binwidth=5)
	plt.show()
except ValueError:
	print('Nope')