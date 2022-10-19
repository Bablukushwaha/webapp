from django.contrib import admin
from django.urls import path
from login import views as login_views
from signup import views as signUp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.home, name=' home'),
    path('login/', login_views.login, name=' login'),
    path('signup/', signUp_views.signup, name='signup'),
    path('contact/', signUp_views.contact, name='contact'),
]
