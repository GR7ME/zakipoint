from django.http import HttpResponse
from .serializers import AdminsSerializer
from rest_framework.renderers import JSONRenderer
from .models import Admins

# Create your views here.
# views.py

def signin_view(request):
    return HttpResponse('Signin part run successfully')


def admins_view(request):
    admins = Admins.objects.all()
    serializer = AdminsSerializer(admins, many=True)
    serialized_data = JSONRenderer().render(serializer.data)
    return HttpResponse(serialized_data, content_type='application/json') 


