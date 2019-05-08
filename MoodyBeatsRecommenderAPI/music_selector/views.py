from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import FormView, CreateView

# from newsletter.models import Join
from newsletter.forms import JoinForm

# def home(request):
# 	return render(request, "home.html", {})

class HomeView(SuccessMessageMixin, CreateView):
	template_name = 'home.html'
	form_class = JoinForm
	success_url = '/'

	def get_success_message(self, cleaned_data):
		return "Thank you for joining MoodiBeats API!"

	# def form_valid(self, form):
	# 	email = form.cleaned_data.get("email")
	# 	# other things with email
	# 	return super(HomeView, self).form_valid(form)
	# Changing the HomeView() parameter to CreateView from FormView
	# allows the form to save the data without having to define form_valid()




