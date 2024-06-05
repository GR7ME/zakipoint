from django.http import HttpResponse
from .serializers import AdminsSerializer,SigninSerializer
from rest_framework.renderers import JSONRenderer
from .models import Admins,Signin

# Create your views here.
# views.py

def signin_view(request):
    signin = Signin.objects.all()
    serializer = SigninSerializer(signin, many=True)
    serialized_data = JSONRenderer().render(serializer.data)
    return HttpResponse(serialized_data, content_type='application/json')


def admins_view(request):
    admins = Admins.objects.all()
    serializer = AdminsSerializer(admins, many=True)
    serialized_data = JSONRenderer().render(serializer.data)
    return HttpResponse(serialized_data, content_type='application/json') 


