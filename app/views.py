
import datetime
from django.shortcuts import render, redirect
from .models import Tutor, Mensaje
from .forms import MensajeForm

from django.views.generic.edit import CreateView





class index(CreateView): 
	model=Mensaje
	form_class = MensajeForm
	template_name = 'app/index.html' 

	def post(self, request ):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
		# <process form cleaned data>
		#return HttpResponseRedirect(reverse_lazy('success') )
			return redirect('index')

