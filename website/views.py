# from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
#from django.core.mail import EmailMessage
#from .decorators import unauthenticated_user
import random
from .forms import *
from .models import *
#import json
import datetime


def home(request):
    context = {}

    return render(request, 'home.html', context)
