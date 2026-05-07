from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # path('post/<int:id>/', views.post_detail, name='post_detail'),
    
    path('',views.landing_view, name='landing_page' ),
    path('signup/',views.signup_view,name='register' ),
    path('login', views.login_view,name='login'),
    path('dashboard',views.dashboard_view,name='dashboard'),
    path('logout', LogoutView.as_view(next_page='landing_page'),name='logout'),
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