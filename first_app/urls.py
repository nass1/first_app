from django.conf.urls import url
from first_app import views

#templates tagging
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^forms/$', views.form_name, name="forms"),
    url(r'^real/$', views.real, name="real"),
    url(r'^other/$', views.other, name="other"),

    url(r'^regi/$', views.regi, name="regi"),

    url(r'^user_login/$', views.user_login, name="user_login"),


]
