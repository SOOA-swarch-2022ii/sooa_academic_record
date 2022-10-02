from rest_framework import serializers
from SOOA_academic_record_ms.models.professoral_record_model import Professoral_record

class Professoral_recordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professoral_record
        fields = ['id','professor_id', 'approved_subjects', 'course_record', 'current_courses', 'campus', 'faculty']
