from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list.as_view()),
    path('snippets/<int:pk>/', views.snippet_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
