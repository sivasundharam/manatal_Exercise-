from .models import School,Student,generateUUID
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

    def update(self, instance, validated_data):
        
        # Update the school instance
       
        instance.name  = validated_data['name']
        instance.no_students = validated_data['no_students']
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def update(self, instance, validated_data):
        
        # Update the Student instance
        print(validated_data)
        instance.first_name  = validated_data['first_name']
        instance.last_name   = validated_data['last_name']
        if 'student_identification' in validated_data:
            instance.student_identification = validated_data['student_identification']
        else:
            instance.student_identification = generateUUID()
        instance.school = validated_data['school']
        instance.save()
        return instance
    
