from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(),name="blogpost-view-create-view"),
    # path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestriy.as_view(),name="update"),
]