from django.shortcuts import redirect, render
import os

def checkCSV(view_func):
	def wrapper_func(request, *args, **kwargs):
		if(os.path.exists(r".\file.csv") == False):
			return render(request, 'EDA/errors/file_not_found.html')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func