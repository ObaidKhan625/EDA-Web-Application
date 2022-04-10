from .models import *
from django.forms import ModelForm

class BarPlotForm(ModelForm):
	class Meta:
		model = BarPlotModel
		fields = '__all__'
		exclude = ['plot_id']

class ScatterPlotForm(ModelForm):
	class Meta:
		model = ScatterPlotModel
		fields = '__all__'
		exclude = ['plot_id']

class LinePlotForm(ModelForm):
	class Meta:
		model = LinePlotModel
		fields = '__all__'
		exclude = ['plot_id']
		
class BoxPlotForm(ModelForm):
	class Meta:
		model = BoxPlotModel
		fields = '__all__'
		exclude = ['plot_id']

class CountPlotForm(ModelForm):
	class Meta:
		model = CountPlotModel
		fields = '__all__'
		exclude = ['plot_id']
		
class HistogramPlotForm(ModelForm):
	class Meta:
		model = HistogramPlotModel
		fields = '__all__'
		exclude = ['plot_id']
