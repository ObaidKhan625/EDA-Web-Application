class BarPlotParameters:
	name = None
	x=None
	y=None
	hue=None
	saturation=None
	errcolor=None
	errwidth=None
	capsize=None
	n_boot=None
	palette=None
	ci=None

	def __init__(self, li):
		self.name = li[0]
		self.x=li[1]
		self.y=li[2]
		self.hue=li[3]
		self.saturation=li[4]
		self.errcolor=li[5]
		self.errwidth=li[6]
		self.capsize=li[7]
		self.n_boot=li[8]
		self.palette=li[9]
		self.ci=li[10]

class ScatterPlotParameters:
	name = None
	x=None
	y=None
	hue=None
	style=None
	size=None 
	palette=None
	legend=None
	n_boot=None
	ci=None

	def __init__(self, li):
		self.name = li[0]
		self.x=li[1]
		self.y=li[2]
		self.hue=li[3]
		self.style=li[4]
		self.size=li[5]
		self.palette=li[6]
		self.legend=li[7]
		self.n_boot=li[8]
		self.ci=li[9]

class LinePlotParameters:
	name = None
	x = None
	y = None
	hue = None
	style = None
	size = None
	n_boot = None
	ci = None
	sort = None
	err_style = None
	legend = None
	palette = None

	def __init__(self, li):
		self.name = li[0]
		self.x = li[1]
		self.y = li[2]
		self.hue = li[3]
		self.style = li[4]
		self.size = li[5]
		self.n_boot = li[6]
		self.ci = li[7]
		self.sort = li[8]
		self.err_style = li[9]
		self.legend = li[10]
		self.palette = li[11]

class CountPlotParameters:
	name = None
	x = None
	hue = None
	saturation = None
	palette = None
	dodge = None

	def __init__(self, li):
		self.name = li[0]
		self.x = li[1]
		self.hue = li[2]
		self.saturation = li[3]
		self.palette = li[4]
		self.dodge = li[5]

class HistogramPlotParameters:
	name = None
	x = None
	hue = None
	stat = None
	bins = None
	binwidth = None
	discrete = None
	palette = None
	legend = None
	fill = None
	kde = None
	multiple = None
	element = None
	log_scale = None

	def __init__(self, li):
		self.name = li[0]
		self.x = li[1]
		self.hue = li[2]
		self.stat = li[3]
		self.bins = li[4]
		self.binwidth = li[5]
		self.discrete = li[6]
		self.palette = li[7]
		self.legend = li[8]
		self.fill = li[9]
		self.kde = li[10]
		self.multiple = li[11]
		self.element = li[12]
		self.log_scale = li[13]

class BoxPlotParameters:
	name = None
	x = None
	y = None
	hue = None
	saturation = None
	palette = None
	width = None
	dodge = None
	fliersize = None
	linewidth = None

	def __init__(self, li):
		self.name = li[0]
		self.x = li[1]
		self.y = li[2]
		self.hue = li[3]
		self.saturation = li[4]
		self.palette = li[5]
		self.width = li[6]
		self.dodge = li[7]
		self.fliersize = li[8]
		self.linewidth = li[9]