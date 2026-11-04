from django.contrib import admin
from django.urls import path
from recipe.views import RecipeListView, RecipeCreateView
from lib.views import IndexTemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path('recipe/', RecipeListView.as_view(), name="recipe-index"),
    path('', IndexTemplateView.as_view(), name="index"),
    path('recipe/create', RecipeCreateView.as_view(), name="recipe-create"), 
]
