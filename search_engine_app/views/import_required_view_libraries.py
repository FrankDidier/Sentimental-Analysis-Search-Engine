from django.http import Http404, HttpResponse, HttpResponseRedirect
from search_engine_app.forms import GeneralForms
from search_engine_app.forms import userPortalForms
from search_engine_app.search_web import SearchWeb
from search_engine_project.logger import log
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from search_engine_app.models import Feedback
from search_engine_app.user_permissions import Authentication
from search_engine_app.forms import feedBackForm
from search_engine_app.models import UserPortal
from django.views import View
from search_engine_app.observer_pattern.subject_topic import NewsPublisher
from django.shortcuts import render, redirect
import logging
import traceback
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from search_engine_app.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from search_engine_app.views.home_page_header_view import HomePageIntroView
from search_engine_app.views.newsreader_story_update_view import NewsReaderStoryUpdateView
from search_engine_app.views.user_authentication_view import UsersAuthenticationView
from search_engine_app.views.user_portal_view import UserPortalView
from search_engine_app.views.search_result_view import SearchResultView
from search_engine_app.views.feed_back_view import FeedbackView


