import seaborn as sns
import matplotlib.pyplot as plt

def save_graph(plot, name):
	fig = plot.get_figure()
	fig.savefig(r'.\static\images\graph.png')
	plt.close('all')

def bar_plot(df, li):
	global name
	name = li[1]
	li[5] = max(min(1, float(li[5])), 0)
	li[7] = max(min(3, float(li[7])), 1)
	li[8] = max(min(0.4, float(li[8])), 0)
	li[11] = max(min(99, int(li[11])), 1)
	plot = sns.barplot(x=str(li[2]), y=str(li[3]), hue=li[4], saturation=li[5], errcolor=li[6], 
		errwidth=li[7], capsize=li[8], n_boot=li[9], palette=li[10], ci=li[11], 
		data=df)
	print(name)
	save_graph(plot, 'Bar Plot')
	return li

def scatter_plot(df, li):
	global name
	name = li[1]
	li[10] = min(99, max(1, int(li[10])))
	plot = sns.scatterplot(x=li[2], y=li[3], hue=li[4], style=li[5], size=li[6], 
		palette=li[7], legend=li[8], n_boot=li[9], ci=li[10], data=df)
	save_graph(plot, 'Scatter Plot')
	return li

def line_plot(df, li):
	global name
	name = li[1]
	li[8] = min(99, max(1, int(li[8])))
	if(li[9] == 'False'):
		li[9] = bool(li[9])
		li[9] = False
	else:
		li[9] = bool(li[9])
		li[9] = True
	plot = sns.lineplot(x=li[2], y=li[3], hue=li[4], style=li[5], size=li[6],
		n_boot=li[7], ci=li[8], sort=li[9], err_style=li[10], legend=li[11], palette=li[12],
		data=df)
	save_graph(plot, 'Line Plot')
	return li

def count_plot(df, li):
	global name
	name = li[1]
	li[4] = min(1, max(0, float(li[4])))
	plot = sns.countplot(x=li[2], hue=li[3], saturation=li[4], palette=li[5], dodge=li[6],
		data=df)
	save_graph(plot, 'Count Plot')
	return li

def hist_plot(df, li):
	#Discrete should be true if element is not auto
	global name
	name = li[1]
	if(li[5] != 'auto'):
		li[5] = int(li[5])
	if(li[7]=='True'):
		li[7] = True
	else:
		li[7] = False
	if(li[10]=='True'):
		li[10] = True
	else:
		li[10] = False
	if(li[11]=='True'):
		li[11] = True
	else:
		li[11] = False
	if(li[14]=='True'):
		li[14] = True
	else:
		li[14] = False
	plot = sns.histplot(x=li[2], hue=li[3], stat=li[4], bins=li[5],binwidth=li[6],
		discrete=li[7], palette=li[8], legend=li[9], fill=li[10], kde=li[11], multiple=li[12], 
		element=li[13], log_scale=li[14], data=df)
	save_graph(plot, 'Histogram')
	return li

def box_plot(df, li):
	global name
	name = li[1]
	if(li[8]=='True'):
		li[8] = True
	else:
		li[8] = False
	li[5] = min(1, max(0, float(li[5])))
	li[7] = float(li[7])
	li[9] = float(li[9])
	plot = sns.boxplot(x=li[2], y=li[3], hue=li[4], saturation=li[5], palette=li[6], width=li[7],
		dodge=li[8], fliersize=li[9], linewidth=li[10], data=df)
	save_graph(plot, 'Box Plot')
	return li