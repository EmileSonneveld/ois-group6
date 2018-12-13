from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^patient_portal$', views.patient_portal, name="patient_portal"),
    url(r'^get_all_patient_symptom$', views.get_all_patient_symptom, name="get_all_patient_symptom"),
    url(r'^get_all_symptom$', views.get_all_symptom, name="get_all_symptom"),
    url(r'^get_all_disease$', views.get_all_disease, name="get_all_disease"),
    url(r'^add_new_symptom_to_patient$', views.add_new_symptom_to_patient, name="add_new_symptom_to_patient"),
]
