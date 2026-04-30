from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]



# from .views import (
#     PostListView, PostDetailView,
#     PostCreateView, PostUpdateView, PostDeleteView
# )

# urlpatterns = [
#     path('', PostListView.as_view(), name='post_list'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
#     path('create/', PostCreateView.as_view(), name='post_create'),
#     path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
#     path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
# ]