from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView


# @api_view(["GET", "POST", "PUT"])
# def home(request):
#     return Response({"name": "sss"})


class Home(APIView):
    def get(self, request):
        return Response({"name": "s1"})
