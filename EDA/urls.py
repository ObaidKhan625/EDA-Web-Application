from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('bar_plot_form/', views.BarPlotFormPage, name='bar_plot_form_page'),
    path('scatter_plot_form/', views.ScatterPlotFormPage, name='scatter_plot_form_page'),
    path('line_plot_form/', views.LinePlotFormPage, name='line_plot_form_page'),
    path('count_plot_form/', views.CountPlotFormPage, name='count_plot_form_page'),
    path('histogram_plot_form/', views.HistogramPlotFormPage, name='histogram_plot_form_page'),
    path('box_plot_form/', views.BoxPlotFormPage, name='box_plot_form_page'),
    path('delete_plot/<str:plot_image_name>', views.deletePlot, name="delete_plot"),
    # path('plot_page/', views.plotPage, name="plot_page"),
]