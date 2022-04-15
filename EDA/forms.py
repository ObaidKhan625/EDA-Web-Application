from .models import *
from django.forms import ModelForm
from django import forms
import pandas as pd

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

class BarPlotForm(forms.Form):
	x = forms.ChoiceField(choices=(), label="x") #f
	y = forms.ChoiceField(choices=(), label="y") #f
	hue = forms.ChoiceField(choices=(), label="hue", required = False) #f
	saturation = forms.FloatField(label="saturation", initial = 0.72) #0 to 1 1 = dark
	errcolor = forms.CharField(label="errcolor", initial = "0.26") #0 to 1 1 = white
	errwidth = forms.FloatField(label="errwidth", initial = 3) # 1-3 recomm
	capsize = forms.FloatField(label="capsize", initial = 0) # 0 to 0.4 recomm
	n_boot = forms.IntegerField(label="n_boot", initial = 1000) # number of iter to cal conf int
	palette = forms.ChoiceField(choices=palette_choices(), label="palette")
	ci = forms.IntegerField(label="ci", initial = 95)

	def __init__(self, *args, **kwargs):
		super(BarPlotForm, self).__init__(*args, **kwargs)
		csv_file = pd.read_csv('file.csv')
		choices = [(i, i) for i in csv_file.columns]
		self.fields['x'].choices = choices
		self.fields['y'].choices = choices
		choices.append((None, None))
		self.fields['hue'].choices = choices

class ScatterPlotForm(forms.Form):
	x = forms.ChoiceField(choices=(), label="x") #f
	y = forms.ChoiceField(choices=(), label="y") #f
	hue = forms.ChoiceField(choices=(), label="hue", required = False) #f
	style = forms.ChoiceField(choices=(), label="style", required = False) #f Different shapes of scattered points
	size = forms.ChoiceField(choices=(), label="size", required = False) #f Different sizes of scattered points
	palette = forms.ChoiceField(choices=palette_choices(), label="palette")
	legend = forms.ChoiceField(choices=legend_choices(), label="legend")
	n_boot = forms.IntegerField(label="n_boot", initial = 1000) # number of iter to cal conf int
	ci = forms.IntegerField(label="ci", initial = 95)

	def __init__(self, *args, **kwargs):
		super(ScatterPlotForm, self).__init__(*args, **kwargs)
		csv_file = pd.read_csv('file.csv')
		choices = [(i, i) for i in csv_file.columns]
		self.fields['x'].choices = choices
		self.fields['y'].choices = choices
		choices.append((None, None))
		self.fields['hue'].choices = choices
		self.fields['style'].choices = choices
		self.fields['size'].choices = choices

class LinePlotForm(forms.Form):
	err_style_choices = (
		('band', 'band'),
		('bar', 'bar'),
		)
	x = forms.ChoiceField(choices=(), label="x") #f
	y = forms.ChoiceField(choices=(), label="y") #f
	hue = forms.ChoiceField(choices=(), label="hue", required = False) #f
	style = forms.ChoiceField(choices=(), label="style", required = False) #f Different shapes of scattered points
	size = forms.ChoiceField(choices=(), label="size", required = False) #f Different sizes of scattered points
	n_boot = forms.IntegerField(label="n_boot", initial = 1000) # number of iter to cal conf int
	ci = forms.IntegerField(label="ci", initial = 95)
	sort = forms.ChoiceField(choices=bool_choices(), label="sort") # Sort Values, default is False
	err_style = forms.ChoiceField(choices=err_style_choices, label = "err_style")
	legend = forms.ChoiceField(choices=legend_choices(), label="legend")
	palette = forms.ChoiceField(choices=palette_choices(), label="palette")

	def __init__(self, *args, **kwargs):
		super(LinePlotForm, self).__init__(*args, **kwargs)
		csv_file = pd.read_csv('file.csv')
		choices = [(i, i) for i in csv_file.columns]
		self.fields['x'].choices = choices
		self.fields['y'].choices = choices
		choices.append((None, None))
		self.fields['hue'].choices = choices
		self.fields['style'].choices = choices
		self.fields['size'].choices = choices
		
class BoxPlotForm(forms.Form):
	err_style_choices = (
		('band', 'band'),
		('bar', 'bar'),
		)
	x = forms.ChoiceField(choices=(), label="x") #f
	y = forms.ChoiceField(choices=(), label="y") #f
	hue = forms.ChoiceField(choices=(), label="hue", required = False) #f
	saturation = forms.FloatField(label = "saturation", initial = 0.75) #0 to 1 1 = dark
	palette = forms.ChoiceField(choices=palette_choices(), label="palette")
	width = forms.FloatField(initial=0.8)
	dodge = forms.ChoiceField(choices=bool_choices())
	fliersize = forms.FloatField(initial=5)
	linewidth = forms.FloatField(required = False)

	def __init__(self, *args, **kwargs):
		super(BoxPlotForm, self).__init__(*args, **kwargs)
		csv_file = pd.read_csv('file.csv')
		choices = [(i, i) for i in csv_file.columns]
		self.fields['x'].choices = choices
		self.fields['y'].choices = choices
		choices.append((None, None))
		self.fields['hue'].choices = choices

class CountPlotForm(forms.Form):
	x = forms.ChoiceField(choices=(), label="x") #f
	hue = forms.ChoiceField(choices=(), required = False, label = "hue") #f
	saturation = forms.FloatField(label = "saturation", initial = 0.75) #0 to 1 1 = dark
	palette = forms.ChoiceField(choices=palette_choices(), label="palette")
	dodge = forms.ChoiceField(choices=bool_choices(), label = "dadge")

	def __init__(self, *args, **kwargs):
		super(CountPlotForm, self).__init__(*args, **kwargs)
		csv_file = pd.read_csv('file.csv')
		choices = [(i, i) for i in csv_file.columns]
		self.fields['x'].choices = choices
		choices.append((None, None))
		self.fields['hue'].choices = choices
		
class HistogramPlotForm(forms.Form):
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
	x = forms.ChoiceField(choices=(), label="x") #f
	hue = forms.ChoiceField(choices=(), label="hue", required = False) #f
	stat = forms.ChoiceField(choices=stat_choices, initial='count', label = "stat")
	bins = forms.CharField(max_length=200, initial='auto', label = "bins")
	binwidth = forms.IntegerField(label = "binwidth", required = False)
	discrete = forms.ChoiceField(choices=bool_choices(), label = "discrete")
	palette = forms.ChoiceField(choices=palette_choices(), label = "palette")
	legend = forms.ChoiceField(choices=legend_choices(), label = "legend")
	fill = forms.ChoiceField(choices=bool_choices(), label = "fill")
	kde = forms.ChoiceField(choices=bool_choices(), label = "kde")
	multiple = forms.ChoiceField(choices=multiple_choices, label = "multiple")
	element = forms.ChoiceField(choices=element_choices, label = "element")
	log_scale = forms.ChoiceField(choices=bool_choices(), label = "log_scale")

	def __init__(self, *args, **kwargs):
		super(HistogramPlotForm, self).__init__(*args, **kwargs)
		csv_file = pd.read_csv('file.csv')
		choices = [(i, i) for i in csv_file.columns]
		self.fields['x'].choices = choices
		choices.append((None, None))
		self.fields['hue'].choices = choices