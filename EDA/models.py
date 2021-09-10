from django.db import models
import os
import pandas as pd

df = None
exists = 0

if(os.path.exists(r".\file.csv") == True):
	exists = 1
	df = pd.read_csv(r".\file.csv")

def feature_tuples():
	global df
	if(exists == 0):
		return (('a', 'a'), ('b', 'b'))
	features = df.columns
	features_li = []
	for i in features:
		if i != 'Unnamed: 0':
			features_li.append(tuple([i, i]))
	features = tuple(features_li)
	return features

def estimator_tuples():
	estimator_tuple = (
		('mean', 'mean'),
		('median', 'median'),
		)
	return estimator_tuple

def palette_choices():
	palette_choice = (
		('rocket', 'rocket'),
		('mako', 'mako'),
		('flare', 'flare'),
		('crest', 'crest'),
		('magma', 'magma'),
		('viridis', 'viridis'),
		('icefire', 'icefire'),
		('inferno', 'inferno'),
		('hot', 'hot'),
		)
	return palette_choice

def legend_choices():
	legend_choice = (
		('auto', 'auto'),
		('brief', 'brief'),
		('full', 'full'),
		)
	return legend_choice

def bool_choices():
	bool_choice = (
		('True', True),
		('False', False),
		)
	return bool_choice

# Create your models here.
class BarPlotModel(models.Model):
	name = models.CharField(max_length=200, default="Bar Plot", primary_key=True)
	x = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	y = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	hue = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f
	saturation = models.FloatField(default=0.75) #0 to 1 1 = dark
	errcolor = models.CharField(max_length=200, default='0.26') #0 to 1 1 = white
	errwidth = models.FloatField(max_length=200, default=3) # 1-3 recomm
	capsize = models.FloatField(max_length=200, default=0) # 0 to 0.4 recomm
	n_boot = models.IntegerField(default = 1000) # number of iter to cal conf int
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	ci = models.IntegerField(default=95)
	
	def __str__(self):
		return self.name

class ScatterPlotModel(models.Model):
	name = models.CharField(max_length=200, default="Scatter Plot", primary_key=True)
	x = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	y = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	hue = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f
	style = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f Different shapes of scattered points
	size = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f Different sizes of scattered points
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	legend = models.CharField(max_length=200, default='auto', choices=legend_choices())
	n_boot = models.IntegerField(default=1000) # number of iter to cal conf int
	ci = models.IntegerField(default=95)
	
	def __str__(self):
		return 'Scatter Plot'

class LinePlotModel(models.Model):
	err_style_choices = (
		('band', 'band'),
		('bar', 'bar'),
		)
	name = models.CharField(max_length=200, default="Line Plot", primary_key=True)
	x = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	y = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	hue = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f
	style = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f Different shapes of scattered points
	size = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f Different sizes of scattered points
	n_boot = models.IntegerField(default=1000) # number of iter to cal conf int
	ci = models.IntegerField(default=95)
	sort = models.CharField(max_length=200, default='False', choices=bool_choices()) # Sort Values, default is False
	err_style = models.CharField(max_length=200, default='band', choices=err_style_choices)
	legend = models.CharField(max_length=200, default='auto', choices=legend_choices())
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	
	def __str__(self):
		return 'Line Plot'
	
class CountPlotModel(models.Model):
	name = models.CharField(max_length=200, default="Count Plot", primary_key=True)
	x = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	hue = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f
	saturation = models.FloatField(default=0.75) #0 to 1 1 = dark
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	dodge = models.CharField(max_length = 200, choices=bool_choices(), default=True)
	
	def __str__(self):
		return 'Count Plot'

class HistogramPlotModel(models.Model):
	stat_choices = (
		('count', 'count'),
		('frequency', 'frequency'),
		('density', 'density'),
		('probability', 'probability'),
		)
	multiple_choices = (
		('layer', 'layer'),
		('dodge', 'dodge'),
		('stack', 'stack'),
		('fill', 'fill'),
		)
	element_choices = (
		('bars', 'bars'),
		('step', 'step'),
		('poly', 'poly'),
		)
	name = models.CharField(max_length=200, default="Histogram", primary_key=True)
	x = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	hue = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f
	stat = models.CharField(max_length=200, null=True, choices=stat_choices, default='count')
	bins = models.CharField(max_length=200, default='auto')
	binwidth = models.IntegerField(blank=True, null=True)
	discrete = models.CharField(max_length=200, default=True, choices=bool_choices())
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	legend = models.CharField(max_length=200, default='auto', choices=legend_choices())
	fill = models.CharField(max_length = 200, null = True, choices=bool_choices(), default=True)
	kde = models.CharField(max_length=200, default=False, choices=bool_choices())
	multiple = models.CharField(max_length=200, null=True, choices=multiple_choices, default='layer')
	element = models.CharField(max_length=200, null=True, choices=element_choices, default='bars')
	log_scale = models.CharField(max_length=200, default=False, choices=bool_choices())
	
	def __str__(self):
		return 'Histogram Plot'

class BoxPlotModel(models.Model):
	name = models.CharField(max_length=200, default="Box Plot", primary_key=True)
	x = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	y = models.CharField(max_length=200, null=True, choices=feature_tuples()) #f
	hue = models.CharField(max_length=200, null=True, blank=True, choices=feature_tuples()) #f
	saturation = models.FloatField(default=0.75)
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	width = models.FloatField(default=0.8)
	dodge = models.CharField(max_length=200, null=True, choices=bool_choices(), default='True')
	fliersize = models.FloatField(default=5)
	linewidth = models.FloatField(null=True, blank=True)
	
	def __str__(self):
		return 'Box Plot'