from .decorators import *
from .forms import *
from .graph_making import *
from .models import *
from .Plot_features import *
import csv, io
from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from os.path import dirname, abspath
import os
import seaborn as sns
# Create your views here.

@checkCSV
def home(request):
	return render(request, 'EDA/dashboard.html')

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
			form.save()
			try:
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
	os.remove(r'.\static\images\graph.png')
	return redirect('/')

def plotPage(request):
	return render(request, 'EDA/plotpage.html')