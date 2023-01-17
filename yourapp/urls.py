from django.conf.urls import url
from . import views

app_name = 'yourapp'

urlpatterns = [
    url(r'^wind_turbines/?$', views.WindTurbinesList.as_view()),  # DONE #SIMPLE
    url(r'^wind_turbines/create/?$', views.WindTurbinesCreate.as_view()),  # DONE #SIMPLE
    url(r'wind_turbines/put/(?P<pk>\d+)/?$', views.WindTurbinesUpdate.as_view()),  # DONE #SIMPLE

    url(r'^employers/?$', views.EmployersList.as_view()),  # DONE #SIMPLE
    url(r'^employers/create/?$', views.EmployersCreate.as_view()),  # DONE #SIMPLE
    url(r'employers/put/(?P<pk>\d+)/?$', views.EmployersUpdate.as_view()),  # DONE #SIMPLE

    url(r'^department/?$', views.DepartmentsList.as_view()),  # DONE #SIMPLE
    url(r'^department/create/?$', views.DepartmentsCreate.as_view()),  # DONE #SIMPLE
    url(r'department/put/(?P<pk>\d+)/?$', views.DepartmentsUpdate.as_view()),  # DONE #SIMPLE

    url(r'^roles/?$', views.RolesList.as_view()),  # DONE #SIMPLE
    url(r'^roles/create/?$', views.RolesCreate.as_view()),  # DONE #SIMPLE
    url(r'roles/put/(?P<pk>\d+)/?$', views.RolesUpdate.as_view()),  # DONE #SIMPLE

]
