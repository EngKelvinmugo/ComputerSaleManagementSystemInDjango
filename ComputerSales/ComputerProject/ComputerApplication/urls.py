from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage , name='home'),
    path('register', views.register, name= "register"),
     path('login/', views.login_page, name= "login"),
    path('logout', views.userLogout, name='logout'),
       path('dashboard', views.dashboard, name='dashboard'),
         path('laptops',views.laptops , name='laptops'),
           path('contact',views.contact , name='contact'),
             path('about',views.about , name='about'),
               path('checkout',views.checkout , name='checkout'),
    
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)