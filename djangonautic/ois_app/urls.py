from django.conf.urls import url
from . import views

app_name = 'ois_app'


urlpatterns = [
    url(r'^git_pull/$', views.git_pull, name="git_pull"),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^patient_portal$', views.patient_portal, name="patient_portal"),
    url(r'^get_all_patient_symptom$', views.get_all_patient_symptom, name="get_all_patient_symptom"),
    url(r'^get_all_symptom$', views.get_all_symptom, name="get_all_symptom"),
    url(r'^get_all_disease$', views.get_all_disease, name="get_all_disease"),
    url(r'^add_new_symptom_to_patient$', views.add_new_symptom_to_patient, name="add_new_symptom_to_patient"),
    url(r'^update_diagnosis$', views.update_diagnosis, name="update_diagnosis"),
    url(r'^symptom/create$', views.symptom_create, name="symptom_create"),
    url(r'^symptom/(?P<slug>[\w-]+)/$', views.symptom_detail, name="symptom_detail"),
    url(r'^symptom/symptom_list_as_doctor', views.symptom_list_as_doctor, name="symptom_list_as_doctor"),
    url(r'^symptom/', views.symptom_list_as_patient, name="symptom_list_as_patient"),
    url(r'^$', views.homepage, name="home"),
    url(r'^articles/$', views.article_list, name="list"),
    url(r'^articles/create$',views.article_create, name="create"),
    url(r'^articles/(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
