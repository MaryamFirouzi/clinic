from rest_framework import serializers
from health.models import Clinic , Doctor
from django.conf import settings
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import delete

class clinicsserializers(serializers.ModelSerializer):
    
    doctor_name = serializers.SerializerMethodField()

    def get_doctor_name(self, obj):
        return obj.doctor.values_list('name', flat=True) 
        
    thumbnail = serializers.SerializerMethodField()
    
    def get_thumbnail(self, obj):
        width = self.context.get('width') or settings.DEFAULT_WIDTH
        height = self.context.get('height') or settings.DEFAULT_HEIGHT
        if obj.top_img:
            im = get_thumbnail(obj.top_img, f'{width}x{height}', crop='center', quality=99)
            return im.url
        return ''    

    class Meta:
        model = Clinic
        fields = '__all__' 

