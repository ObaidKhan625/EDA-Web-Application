from .decorators import *
from .forms import *
from .graph_making import *
from .models import *
from .Plot_features import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from os.path import dirname, abspath
import csv
import io
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import uuid
# Create your views here.

# @checkCSV
def home(request):
	if(request.method == "POST"):
		csv_file = request.FILES["file"]
		file_data = csv_file.read().decode("utf-8")	
		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		# field names 
		fields = lines[0].split(",")
		dict = {}
		for i in fields:
			dict[i] = []
		for i in range(1, len(lines)-1):
			for j in range(len(fields)):
				try:
					k = lines[i].split(",")
					dict[fields[j]].append(k[j])
				except:
					return render(request, 'EDA/errors/file_not_found.html')
		df = pd.DataFrame(dict)

		# saving the dataframe 
		df.to_csv('file.csv') 
		return render(request, 'EDA/dashboard.html')
	return render(request, 'EDA/home.html')

def BarPlotFormPage(request):
	form = BarPlotForm()
	if request.method == 'POST':
		form = BarPlotForm(request.POST)
		if form.is_valid():
			try:
				plot_image_name = uuid.uuid4()
				li = make_graph(request.POST, 1, plot_image_name)
				deleteGraph('Bar Plot')
				graph = BarPlotParameters(li)
				context = {'graph': graph, 'plot_image_name': str(plot_image_name)+'.png'}
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
				plot_image_name = uuid.uuid4()
				li = make_graph(request.POST, 2, plot_image_name)
				graph = ScatterPlotParameters(li)
				context = {'graph': graph, 'plot_image_name': str(plot_image_name)+'.png'}
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
				plot_image_name = uuid.uuid4()
				li = make_graph(request.POST, 3, plot_image_name)
				graph = LinePlotParameters(li)
				context = {'graph': graph, 'plot_image_name': str(plot_image_name)+'.png'}
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
				plot_image_name = uuid.uuid4()
				li = make_graph(request.POST, 4, plot_image_name)
				graph = CountPlotParameters(li)
				context = {'graph': graph, 'plot_image_name': str(plot_image_name)+'.png'}
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
				plot_image_name = uuid.uuid4()
				li = make_graph(request.POST, 5, plot_image_name)
				graph = HistogramPlotParameters(li)
				context = {'graph': graph, 'plot_image_name': str(plot_image_name)+'.png'}
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
				plot_image_name = uuid.uuid4()
				li = make_graph(request.POST, 6, plot_image_name)
				graph = BoxPlotParameters(li)
				context = {'graph': graph, 'plot_image_name': str(plot_image_name)+'.png'}
				return render(request, 'EDA/plots/box_plot.html', context)
			except:
				return render(request, 'EDA/errors/plot_error.html')
	context = {'form':form}
	return render(request, 'EDA/forms/box_plot_form.html', context)

# Helper functions
def deletePlot(request, plot_image_name):
	image_path = ".\static\images\\" + plot_image_name
	os.remove(image_path)
	return redirect('/')

# def plotPage(request):
# 	return render(request, 'EDA/plotpage.html')