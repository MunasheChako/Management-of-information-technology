from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models

# Create your views here.



def about(request):
  return render(request, 'about.html', {'title': 'about page'})

class RecipeListView(ListView):
  model = models.Recipe
  template_name = 'home.html'
  context_object_name = 'recipes'

class RecipeDetailView(DetailView):
  model = models.Recipe
  template_name = 'recipe_detail.html'

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  success_url = reverse_lazy('home')
  template_name = 'confirm_delete.html'

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
  model = models.Recipe
  fields = ['title', 'description']
  template_name = 'recipe_form.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Recipe
  fields = ['title', 'description']
  template_name = 'recipe_form.html'

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)  







