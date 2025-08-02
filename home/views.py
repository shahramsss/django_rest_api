from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .serializers import PersonSerializer
from .models import Person


# @api_view(["GET", "POST", "PUT"])
# def home(request):
#     return Response({"name": "sss"})


class Home(APIView):
    def get(self, request):
        # http://127.0.0.1:8000/home/?name=aaa
        # name = request.GET['name']
        name = request.query_params["name"]
        return Response({"name": name})

    def post(self, request):
        name = request.data["name"]
        return Response({"name": name})


class PersonView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(persons, many=True)
        return Response(
            data=ser_data.data
        )
