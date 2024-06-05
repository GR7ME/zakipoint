from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import AdminsSerializer, SigninSerializer
from rest_framework.renderers import JSONRenderer
from .models import Admins, Signin

# Create your views here.
# views.py


@api_view(["GET"])
def signin_view(request):
    signin = Signin.objects.all()
    serializer = SigninSerializer(signin, many=True)
    serialized_data = JSONRenderer().render(serializer.data)
    return HttpResponse(serialized_data, content_type="application/json")


@api_view(["GET"])
def admins_view(request):
    admins = Admins.objects.all()
    serializer = AdminsSerializer(admins, many=True)
    serialized_data = JSONRenderer().render(serializer.data)
    return HttpResponse(serialized_data, content_type="application/json")
