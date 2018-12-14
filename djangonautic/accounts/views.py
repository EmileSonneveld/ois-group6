from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from subprocess import check_output
from . import forms
from .forms import RegistrationForm
from .models import *
import re
import unidecode
import json


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)


def git_pull(request):
    if request.user.is_staff:
        data = check_output(["git", "pull"])
        # data += check_output(["systemctl", "restart", "gunicorn"])  # Doesn't work (no root)
        return HttpResponse(data, content_type='text/plain')
    else:
        return HttpResponse('Nice try.', status=401)


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


@require_http_methods(["GET", "POST"])
@login_required(login_url="/accounts/login/")
def add_new_symptom_to_patient(request):
    if request.method == "POST":
        name_slug = request.POST.get("name_slug")
        user_id = request.user.id
        patientProfile = PatientProfile.objects.get(user__id=user_id)
        symp = Symptom.objects.get(name_slug=name_slug)
        Diagnosis.objects.create(patient=patientProfile, symptom=symp)
        context = {"wasPostRequest": True}
    else:
        context = {"wasPostRequest": False}
    return render(request, 'add_new_symptom_to_patient.html', context)


@csrf_exempt
@require_http_methods(["POST"])
@login_required(login_url="/accounts/login/")
def update_diagnosis(request):
    diagnosis = request.POST.get("diagnosis")
    symptom = request.POST.get("symptom")
    start_date = request.POST.get("start_date")
    end_date = request.POST.get("end_date")
    severity = request.POST.get("severity")

    d = Diagnosis.objects.get(id=diagnosis)
    # d.symptom = symptom
    d.start_date = start_date
    d.end_date = end_date
    d.severity = severity
    d.save()
    return HttpResponse("OK")


@login_required(login_url="/accounts/login/")
def disease_create(request):
    if request.method == 'POST':
        form = forms.CreateDisease(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.added_by = DoctorProfile.objects.get(user=request.user)
            instance.name_slug = slugify(request.POST.get("name"))
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateDisease()
    return render(request, 'disease_create.html', {'form': form})


def disease_list(request):
    diseases_added_by_me = Disease.objects.filter(added_by=1)
    diseases_rest = Disease.objects.exclude(added_by=1)
    return render(request, 'disease_list.html', {
        'diseases_added_by_me': diseases_added_by_me,
        'diseases_rest': diseases_rest
    })


def disease_detail(request, slug):
    obj = Disease.objects.get(name_slug=slug)
    return render(request, 'disease_detail.html', { 'disease': obj })