__author__ = 'dell'


from attendenceapp.models import *
from rest_framework import serializers

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields = '__all__'

'''

class first_serializer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'

class second_serializer1(serializers.ModelSerializer):
    #name=serializers.CharField(max_length=100)


    class Meta:
        model=admin1
        fields='__all__'




class third_serializer1(serializers.ModelSerializer):
    #name=serializers.CharField(max_length=100)


    class Meta:
        model=hod
        fields='__all__'
class fourth_serializerl(serializers.ModelSerializer):
    class Meta:
        model=admin1
        fields='__all__'
class fifth_serializer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'
class sixth_serializerl(serializers.ModelSerializer):
    class Meta:
        model=sunbject
        fields='__all__'
class seventh_serializerl(serializers.ModelSerializer):
    class Meta:
        model=collage
        fields="__all__"
class eight_serializerl(serializers.ModelSerializer):
    class Meta:
        model=department
        fields='__all__'



class loginserial(serializers.Serializer):
    Key=serializers.CharField(max_length=40)
    password=serializers.CharField(max_length=40)
class loginteacher(serializers.Serializer):
    Key=serializers.CharField(max_length=199)
    password=serializers.CharField(max_length=100)


class loginadmin(serializers.Serializer):
    Key=serializers.CharField(max_length=199)
    password=serializers.CharField(max_length=100)
class loginhod(serializers.Serializer):
    Key=serializers.CharField(max_length=199)
    password=serializers.CharField(max_length=100)
class totaldepartment(serializers.ModelSerializer):
    class Meta:
        model=hod
        fields='__all__'

'''