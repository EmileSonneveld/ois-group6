from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$',views.signup_view,name="signup"),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',views.logout_view,name="logout"),
    url(r'^patient_portal$', views.patient_portal, name="patient_portal"),
    url(r'^get_patient_symptoms$', views.get_patient_symptoms, name="get_patient_symptoms"),
    url(r'^get_all_symptoms$', views.get_all_symptoms, name="get_all_symptoms"),
]
