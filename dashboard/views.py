# from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
import random
from .forms import *
from .models import *
import datetime


class AdminDashView(View):
    def render(self, request):
        return render(request, 'Portal/home1.html')

    def post(self, request):
        #self.form = PostForm(request.POST)
        # if self.form.is_valid():
        # self.form.save()
        # return redirect('post_list')
        return self.render(request)

    def get(self, request):
        #self.form = PostForm()
        return self.render(request)


class TeacherDashView(View):
    def render(self, request):
        return render(request, 'Portal/Admin/error-401.html')

    def post(self, request):
        #self.form = PostForm(request.POST)
        # if self.form.is_valid():
        # self.form.save()
        # return redirect('post_list')
        return self.render(request)

    def get(self, request):
        #self.form = PostForm()
        return self.render(request)


class ParentDashView(View):
    def render(self, request):
        return render(request, 'Portal/home3.html')

    def post(self, request):
        #self.form = PostForm(request.POST)
        # if self.form.is_valid():
        # self.form.save()
        # return redirect('post_list')
        return self.render(request)

    def get(self, request):
        #self.form = PostForm()
        return self.render(request)
