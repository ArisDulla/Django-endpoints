from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.

# ------ VIEWS TURBINES ----------------------------
#
# GET requests
#
class WindTurbinesList(generics.ListAPIView):
    queryset = Turbines.objects.all()
    serializer_class = TurbinesSerializer

    def get_all(self, request):
        return self.get_queryset()


#
# POST request
#
class WindTurbinesCreate(generics.CreateAPIView):
    queryset = Turbines.objects.all()
    serializer_class = TurbinesSerializer

    def set(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#
# PUT request
#
class WindTurbinesUpdate(generics.UpdateAPIView):
    queryset = Turbines.objects.all()
    serializer_class = TurbinesSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# -----------------------------------------------------------
# Employers
#
class EmployersList(generics.ListAPIView):
    queryset = Employers.objects.all()
    serializer_class = EmployersSerializer

    def get_all(self, request):
        return self.get_queryset()


#
# POST request
#
class EmployersCreate(generics.CreateAPIView):
    queryset = Employers.objects.all()
    serializer_class = EmployersSerializer

    def set(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#
# PUT request
#
class EmployersUpdate(generics.UpdateAPIView):
    queryset = Employers.objects.all()
    serializer_class = EmployersSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# ----------------------------------------
# Departments
#
class DepartmentsList(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

    def get_all(self, request):
        return self.get_queryset()


#
# POST request
#
class DepartmentsCreate(generics.CreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

    def set(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#
# PUT request
#
class DepartmentsUpdate(generics.UpdateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# -----------------------------------------------------
#  ROLE
#
class RolesList(generics.ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

    def get_all(self, request):
        return self.get_queryset()


#
# POST request
#
class RolesCreate(generics.CreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

    def set(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#
# PUT request
#
class RolesUpdate(generics.UpdateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
