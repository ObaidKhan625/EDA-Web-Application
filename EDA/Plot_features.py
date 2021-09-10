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
		self.name = li[1]
		self.x=li[2]
		self.y=li[3]
		self.hue=li[4]
		self.saturation=li[5]
		self.errcolor=li[6]
		self.errwidth=li[7]
		self.capsize=li[8]
		self.n_boot=li[9]
		self.palette=li[10]
		self.ci=li[11]

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
		self.name = li[1]
		self.x=li[2]
		self.y=li[3]
		self.hue=li[4]
		self.style=li[5]
		self.size=li[6]
		self.palette=li[7]
		self.legend=li[8]
		self.n_boot=li[9]
		self.ci=li[10]

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
		self.name = li[1]
		self.x = li[2]
		self.y = li[3]
		self.hue = li[4]
		self.style = li[5]
		self.size = li[6]
		self.n_boot = li[7]
		self.ci = li[8]
		self.sort = li[9]
		self.err_style = li[10]
		self.legend = li[11]
		self.palette = li[12]

class CountPlotParameters:
	name = None
	x = None
	hue = None
	saturation = None
	palette = None
	dodge = None

	def __init__(self, li):
		self.name = li[1]
		self.x = li[2]
		self.hue = li[3]
		self.saturation = li[4]
		self.palette = li[5]
		self.dodge = li[6]

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
		self.name = li[1]
		self.x = li[2]
		self.hue = li[3]
		self.stat = li[4]
		self.bins = li[5]
		self.binwidth = li[6]
		self.discrete = li[7]
		self.palette = li[8]
		self.legend = li[9]
		self.fill = li[10]
		self.kde = li[11]
		self.multiple = li[12]
		self.element = li[13]
		self.log_scale = li[14]

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
		self.name = li[1]
		self.x = li[2]
		self.y = li[3]
		self.hue = li[4]
		self.saturation = li[5]
		self.palette = li[6]
		self.width = li[7]
		self.dodge = li[8]
		self.fliersize = li[9]
		self.linewidth = li[10]