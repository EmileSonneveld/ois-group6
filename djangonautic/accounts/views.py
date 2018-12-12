from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core import serializers
import json

from .forms import RegistrationForm
from .models import *


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            return redirect('articles:list')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')


def patient_portal(request):
    return render(request, 'patient_portal.html')


def query_result_to_array(list_object):
    """
    Returns an object ready to be serialized with json.dumps(res)
    """
    d = dict()
    tmp_python = serializers.serialize('python', list_object)
    for el in tmp_python:
        d[el["pk"]] = el["fields"]
    return d


def get_all_symptom(request):
    q_res = Symptom.objects.all()
    res = query_result_to_array(q_res)
    return JsonResponse(res, json_dumps_params={'indent': 2})


def get_all_disease(request):
    q_res = Disease.objects.all()
    res = query_result_to_array(q_res)
    return JsonResponse(res, json_dumps_params={'indent': 2})


def get_all_patient_symptom(request):
    user_id = request.user.id
    q_res = Diagnosis.objects.filter(patient__user__id=user_id)
    res = query_result_to_array(q_res)
    return JsonResponse(res, json_dumps_params={'indent': 2})

    pp = PatientProfile.objects.get(user=request.user)
    return JsonResponse({
        'user': request.user.__str__(),
        'user.id': request.user.id.__str__(),
        'pp_pk': pp.pk.__str__(),
        'pp_str': pp.__str__(),
        'q_res': len(q_res).__str__(),
    })
