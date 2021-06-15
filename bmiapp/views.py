from django import forms
from bmiapp.forms import UserForm
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def new(request):
	params = {'answer': '', 'tall': '', 'weight': '', 'form': None}
	if request.method =='POST':
		form = UserForm(request.POST)
		params['tall'] = request.POST['tall']
		params['weight'] = request.POST['weight']
		params['answer'] = 'あなたのBMIは' + str(round(float(request.POST['weight'])/(float(request.POST['tall'])/100)**2, 2)) + 'です。'
		params['form'] = form
		params['BMI1'] = "＜ " + str(round(((float(request.POST['tall'])/100)**2)*18.5, 2))
		params['BMI2'] = str(round(((float(request.POST['tall'])/100)**2)*18.5, 2)) + " ～ " + str(round(((float(request.POST['tall'])/100)**2)*25, 2))
		params['BMI3'] = str(round(((float(request.POST['tall'])/100)**2)*25, 2)) + " ～ " + str(round(((float(request.POST['tall'])/100)**2)*30, 2))
		params['BMI4'] = str(round(((float(request.POST['tall'])/100)**2)*30, 2)) + " ～ " + str(round(((float(request.POST['tall'])/100)**2)*35, 2))
		params['BMI5'] = str(round(((float(request.POST['tall'])/100)**2)*35, 2)) + " ～ " + str(round(((float(request.POST['tall'])/100)**2)*40, 2))
		params['BMI6'] = str(round(((float(request.POST['tall'])/100)**2)*40, 2)) + " ≦"
	else:
		params['form'] = UserForm
	return render(request, 'bmiapp/new.html', params)

#class BmiPage(TemplateView):
#	template_name = 'bmi.html'