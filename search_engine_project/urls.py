"""search_engine_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from search_engine_app import views
from django.conf.urls import  url, include
from search_engine_app.views.import_required_view_libraries import *
from django.contrib import admin



""""file modified to view factory pattern
@Author: Adarsh Koppa Manjunath"""



class URLFactory:

    def get_view_functions():
       

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('search_engine_app/',SearchResultView.search),
            path('search_engine_app/home.html', SearchResultView.search),
            path('search_engine_app/ise.html', HomePageIntroView.ise),
            path('search_engine_app/projectTeam.html', HomePageIntroView.projectTeam),
            path('search_engine_app/login.html', UsersAuthenticationView.loginPage, name ='login'),
            path('search_engine_app/register.html',  UsersAuthenticationView.registerPage),
            path("search_engine_app/logout", UsersAuthenticationView.logoutUser, name="logout"),
            path("search_engine_app/userPortal.html",UserPortalView.userPortal),
            path("search_engine_app/viewYourUpdatedResults.html",NewsReaderStoryUpdateView.viewYourUpdatedResult),
            path("search_engine_app/feedBack.html",FeedbackView.feedback_view),
            path("search_engine_app/feedback_login.html",UsersAuthenticationView.feedback_login_view),
         
            
            
        ]
        return urlpatterns
view_factory_obj=URLFactory
urlpatterns=view_factory_obj.get_view_functions()


