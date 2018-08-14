from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class EstudanteView(TemplateView):
	template_name = 'index.html'

class NotaView(TemplateView):
	template_name = 'nota.html'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)	    
	    return context

