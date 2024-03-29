from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('', views.dashboard, name='dashboard'),
    path('blog/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
    path('add-appointment/<int:pk>', views.add_appointment, name='add-appointment'),
    path('appointments/', views.appointment, name='appointment')
]
