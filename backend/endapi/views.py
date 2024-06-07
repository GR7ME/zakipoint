from rest_framework.decorators import api_view
from rest_framework import generics
from django.http import HttpResponse
from .serializers import AdminsSerializer, SigninSerializer, LogSerializer
from rest_framework.renderers import JSONRenderer
from .models import Admins, Signin, LogEntry
from .utils import generate_pyspark_log

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


def generate_logs_view(request):
    log_group = generate_pyspark_log()

    for key, value in log_group.items():
        if key == "LOG GROUP":
            for log_type, logs in value.items():
                for log in logs.get("LOGS", []):
                    LogEntry.objects.create(
                        timestamp=log["TIMESTAMP"],
                        message_status=log["MESSAGE STATUS"],
                        message=log["MESSAGE"],
                        log_group=log_type,
                        log_id=key,
                    )
        else:
            for log in value:
                LogEntry.objects.create(
                    timestamp=log["TIMESTAMP"],
                    message_status=log["MESSAGE STATUS"],
                    message=log["MESSAGE"],
                    log_group=log_type,
                    log_id=key,
                )

    return HttpResponse("Logs generated and saved to database")


class LogListView(generics.ListCreateAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogSerializer
