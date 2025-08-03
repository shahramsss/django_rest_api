from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .serializers import PersonSerializer, AnswerSerializer, QuestionSerializer
from .models import Person, Question, Answer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(persons, many=True)
        return Response(data=ser_data.data)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestionSerializer(
            instance=question, data=request.data, partial=True
        )
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({"message": "question deleted"})
