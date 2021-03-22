import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3, 4, 5]
y = [3, 2, 4, 5, 3]

plot = sns.scatterplot(x=x, y=y)
plt.show()
plt.clf()

plot = sns.lineplot(x=x, y=y)
plt.show()