import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def save_graph(plot, plot_image_name):
	fig = plot.get_figure()
	image_path = ".\static\images\\" + str(plot_image_name) + ".png"
	fig.savefig(image_path)
	plt.close('all')

def bar_plot(li, plot_image_name):
	df = pd.read_csv('file.csv')
	li[4] = max(min(1, float(li[4])), 0)
	li[6] = max(min(3, float(li[6])), 1)
	li[7] = max(min(0.4, float(li[7])), 0)
	li[10] = max(min(99, int(li[10])), 1)
	plot = sns.barplot(x=li[1], y=li[2], hue=li[3], saturation=li[4], errcolor=li[5], 
		errwidth=li[6], capsize=li[7], n_boot=li[8], palette=li[9], ci=li[10], 
		data=df)
	save_graph(plot, plot_image_name)
	return li

def scatter_plot(li, plot_image_name):
	df = pd.read_csv('file.csv')
	li[9] = min(99, max(1, int(li[9])))
	plot = sns.scatterplot(x=li[1], y=li[2], hue=li[3], style=li[4], size=li[5], 
		palette=li[6], legend=li[7], n_boot=li[8], ci=li[9], data=df)
	save_graph(plot, plot_image_name)
	return li

def line_plot(li, plot_image_name):
	df = pd.read_csv('file.csv')
	li[7] = min(99, max(1, int(li[7])))
	if(li[8] == 'False'):
		li[8] = bool(li[8])
		li[8] = False
	else:
		li[8] = bool(li[8])
		li[8] = True
	plot = sns.lineplot(x=li[1], y=li[2], hue=li[3], style=li[4], size=li[5],
		n_boot=li[6], ci=li[7], sort=li[8], err_style=li[9], legend=li[10], palette=li[11],
		data=df)
	save_graph(plot, plot_image_name)
	return li

def count_plot(li, plot_image_name):
	df = pd.read_csv('file.csv')
	li[3] = min(1, max(0, float(li[3])))
	if(li[5]=='True'):
		li[5] = True
	else:
		li[5] = False
	plot = sns.countplot(x=li[1], hue=li[2], saturation=li[3], palette=li[4], dodge=li[5],
		data=df)
	save_graph(plot, plot_image_name)
	return li

def hist_plot(li, plot_image_name):
	df = pd.read_csv('file.csv')
	#Discrete should be true if element is not auto
	if(li[4] != 'auto'):
		li[4] = int(li[4])
	if(li[6]=='True'):
		li[6] = True
	else:
		li[6] = False
	if(li[9]=='True'):
		li[9] = True
	else:
		li[9] = False
	if(li[10]=='True'):
		li[10] = True
	else:
		li[10] = False
	if(li[13]=='True'):
		li[13] = True
	else:
		li[13] = False
	plot = sns.histplot(x=li[1], hue=li[2], stat=li[3], bins=li[4],binwidth=li[5],
		discrete=li[6], palette=li[7], legend=li[8], fill=li[9], kde=li[10], multiple=li[11], 
		element=li[12], log_scale=li[13], data=df)
	save_graph(plot, plot_image_name)
	return li

def box_plot(li, plot_image_name):
	df = pd.read_csv('file.csv')
	if(li[7]=='True'):
		li[7] = True
	else:
		li[7] = False
	li[4] = min(1, max(0, float(li[4])))
	li[6] = float(li[6])
	li[8] = float(li[8])
	plot = sns.boxplot(x=li[1], y=li[2], hue=li[3], saturation=li[4], palette=li[5], width=li[6],
		dodge=li[7], fliersize=li[8], linewidth=li[9], data=df)
	save_graph(plot, plot_image_name)
	return li