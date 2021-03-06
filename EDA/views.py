from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv, io
from .forms import *
from .models import *
from os.path import dirname, abspath
import string, random
import os
from .Plot_features import *
from .decorators import *
name = 'abc'

def save_graph(plot):
	fig = plot.get_figure()
	fig.savefig(r'C:\Users\OBAID\OneDrive\Desktop\EDA-Web-Application\static\images\graph.png')
	plt.close('all')

def make_graph(a, num):
	li = []
	for i in a:
		if(a[i]==''):
			li.append(None)
		else:
			li.append(a[i])

	if(num == 1):
		return bar_plot(df, li)

	elif(num == 2):
		return scatter_plot(df, li)

	elif(num == 3):
		return line_plot(df, li)

	elif(num == 4):
		return count_plot(df, li)

	elif(num == 5):
		return hist_plot(df, li)

	else:
		return box_plot(df, li)

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
	save_graph(plot)
	return li

def scatter_plot(df, li):
	global name
	name = li[1]
	li[10] = min(99, max(1, int(li[10])))
	plot = sns.scatterplot(x=li[2], y=li[3], hue=li[4], style=li[5], size=li[6], 
		palette=li[7], legend=li[8], n_boot=li[9], ci=li[10], data=df)
	save_graph(plot)
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
	save_graph(plot)
	return li

def count_plot(df, li):
	global name
	name = li[1]
	li[4] = min(1, max(0, float(li[4])))
	plot = sns.countplot(x=li[2], hue=li[3], saturation=li[4], palette=li[5], dodge=li[6],
		data=df)
	save_graph(plot)
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
	save_graph(plot)
	return li

@checkCSV
def home(request):
	global df
	if request.method == 'POST':
		try:
			csv_file = request.FILES['file']
			if(csv_file.name[-4:] != '.csv'):
				return render(request, 'EDA/errors/file_not_found.html')
			data_set = csv_file.read().decode('UTF-8')
			io_string = io.StringIO(data_set)
			df = pd.read_csv(io_string, sep=",")
			del df[df.columns[0]]
			df.to_csv(r"C:\Users\OBAID\OneDrive\Desktop\EDA-Web-Application\EDA\file.csv")
		except:
			return render(request, 'EDA/errors/file_not_found.html')
		return render(request, 'EDA/dashboard.html')
	return render(request, 'EDA/home.html')

def BarPlotFormPage(request):
	form = BarPlotForm()
	if request.method == 'POST':
		form = BarPlotForm(request.POST)
		if form.is_valid():
			form.save()
			try:
				li = make_graph(request.POST, 1)
				deleteGraph('Bar Plot')
				b = BarPlotParameters(li)
				context = {'b':b}
				return render(request, 'EDA/plots/bar_plot.html', context)
			except:
				return render(request, 'EDA/errors/plot_error.html')
	context = {'form':form}
	return render(request, 'EDA/forms/bar_plot_form.html', context)

def ScatterPlotFormPage(request):
	form = ScatterPlotForm()
	if request.method == 'POST':
		form = ScatterPlotForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				li = make_graph(request.POST, 2)
				deleteGraph('Scatter Plot')
				b = ScatterPlotParameters(li)
				context = {'b':b}
				return render(request, 'EDA/plots/scatter_plot.html', context)
			except:
				return render(request, 'EDA/errors/plot_error.html')
	context = {'form':form}
	return render(request, 'EDA/forms/scatter_plot_form.html', context)

def LinePlotFormPage(request):
	form = LinePlotForm()
	if request.method == 'POST':
		form = LinePlotForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				li = make_graph(request.POST, 3)
				deleteGraph('Line Plot')
				b = LinePlotParameters(li)
				context = {'b':b}
				return render(request, 'EDA/plots/line_plot.html', context)
			except:
				return render(request, 'EDA/errors/plot_error.html')
	context = {'form':form}
	return render(request, 'EDA/forms/line_plot_form.html', context)

def CountPlotFormPage(request):
	form = CountPlotForm()
	if request.method == 'POST':
		form = CountPlotForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				li = make_graph(request.POST, 4)
				deleteGraph('Count Plot')
				b = CountPlotParameters(li)
				context = {'b':b}
				return render(request, 'EDA/plots/count_plot.html', context)
			except:
				return render(request, 'EDA/errors/plot_error.html')
	context = {'form':form}
	return render(request, 'EDA/forms/count_plot_form.html', context)

def HistogramPlotFormPage(request):
	form = HistogramPlotForm()
	if request.method == 'POST':
		form = HistogramPlotForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				li = make_graph(request.POST, 5)
				deleteGraph('Histogram')
				b = HistogramPlotParameters(li)
				context = {'b':b}
				return render(request, 'EDA/plots/histogram_plot.html', context)
			except:
				return render(request, 'EDA/errors/plot_error.html')
	context = {'form':form}
	return render(request, 'EDA/forms/histogram_plot_form.html', context)

def BoxPlotFormPage(request):
	form = BoxPlotForm()
	if request.method == 'POST':
		form = BoxPlotForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				li = make_graph(request.POST, 6)
				deleteGraph('Box Plot')
				b = BoxPlotParameters(li)
				context = {'b':b}
				return render(request, 'EDA/plots/box_plot.html', context)
			except:
				return render(request, 'EDA/errors/plot_error.html')
	context = {'form':form}
	return render(request, 'EDA/forms/box_plot_form.html', context)

def deletePlot(request):
	#d = dirname(dirname(abspath(__file__)))
	os.remove(r'C:\Users\OBAID\OneDrive\Desktop\EDA-Web-Application\static\images\graph.png')
	return redirect('/')

def deleteGraph(graph_type):
	if(graph_type == 'Bar Plot'):
		graph = BarPlotModel.objects.get(name= name)
		graph.delete()
	elif(graph_type == 'Scatter Plot'):
		graph = ScatterPlotModel.objects.get(name= name)
		graph.delete()
	elif(graph_type == 'Line Plot'):
		graph = LinePlotModel.objects.get(name= name)
		graph.delete()
	elif(graph_type == 'Count Plot'):
		graph = CountPlotModel.objects.get(name= name)
		graph.delete()
	elif(graph_type == 'Histogram'):
		graph = HistogramPlotModel.objects.get(name= name)
		graph.delete()
	else:
		graph = BoxPlotModel.objects.get(name= name)
		graph.delete()

def plotPage(request):
	return render(request, 'EDA/plotpage.html')