from django.shortcuts import render
from django.contrib import messages

from django.views.generic import (TemplateView, CreateView, DetailView)

from .models import Skill, Project, SobreMi


from .forms import ContactForm
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sobremi"] = SobreMi.objects.latest('id')
        context["habilidades"] = Skill.objects.all()
        context["proyectos"] = Project.objects.all()
        return context

class DetailProjectView(DetailView):
    model = Project
    template_name = 'detailproject.html'

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = "/#contacto"

    def form_valid(self, form):
        #Logica del proces
        messages.success(self.request, 'Correo enviado con exito')
        return super(ContactCreateView, self).form_valid(form)


