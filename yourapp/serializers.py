# Create your serializers here

from rest_framework import serializers

from yourapp.models import Turbines, Employers, Departments, Roles
from datetime import datetime


#
# TABLE -- Turbines
#
class TurbinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turbines
        fields = ['id', 'name', 'lat', 'long', 'power']

    def create(self, validated_data):
        user = Turbines(
            name=validated_data['name'],
            lat=validated_data['lat'],
            long=validated_data['long'],
            power=validated_data['power']
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.id)
        instance.lat = validated_data.get('lat', instance.id)
        instance.long = validated_data.get('long', instance.id)
        instance.power = validated_data.get('power', instance.id)

        instance.save()
        return instance


#
# TABLE -- Employers
#
class EmployersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = ['id', 'first_name', 'last_name', 'address', 'age']

    def create(self, validated_data):
        user = Employers(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            age=validated_data['age']
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.age = validated_data.get('age', instance.age)

        instance.save()
        return instance


#
# TABLE -- Departments
#
class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['name', 'roof', 'office']

    def create(self, validated_data):
        user = Departments(
            name=validated_data['name'],
            roof=validated_data['roof'],
            office=validated_data['office']
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roof = validated_data.get('roof', instance.roof)
        instance.office = validated_data.get('office', instance.office)
        instance.employers = validated_data.get('employers', instance.employers)

        instance.save()
        return instance


#
# TABLE -- Departments
#
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['departments', 'employers', 'details']

    def create(self, validated_data):
        user = Roles(
            departments=validated_data['departments'],
            employers=validated_data['employers'],
            date=datetime.now(),
            details=validated_data['details']
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('departments', instance.name)
        instance.roof = validated_data.get('employers', instance.roof)
        instance.employers = validated_data.get('details', instance.employers)

        instance.save()
        return instance
