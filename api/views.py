from rest_framework.response import Response
from rest_framework.decorators import api_view
from crud.models import Question
from crud.serializers import UserSerializer, QuestionSerializer

@api_view(['GET'])
def getData(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)