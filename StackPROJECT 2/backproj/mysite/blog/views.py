from django.contrib.auth import authenticate, logout
from django.db.models import Exists, OuterRef,Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

from .forms import Sign_Up_Form
from .models import Question
from .serializers import *
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def sign_up(request):
    user_form = Sign_Up_Form(request.data)
    print(request.data)
    if user_form.is_valid():
        user_form.save()
        return Response({"message": "Success"}, status=status.HTTP_200_OK)
    else:
        return Response({"errors": user_form.errors}, status=status.HTTP_400_BAD_REQUEST)
#
# {
# "first_name":"Poxos",
# "last_name":"Poxosyan",
# "username":"Poxos123",
# "password1":"pp123pp.",
# "password2":"pp123pp.",
# "email":"pp@gmail.com"
# }

from django.contrib.auth import authenticate

@api_view(['POST'])
def sign_in(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'message': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        print(f"Authentication failed for username: {username}")
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

# {
# "username": "Poxos123",
# "password": "pp123pp."
# }


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_question(request):
    print(request.user)

    serializer = AddQuestionSerializer(data=request.data, context={'user': request.user})
    print(serializer.is_valid())
    if serializer.is_valid():
        new = serializer.save()
        print("new", new)
        new_serial = QuestionSerial(new)
        print(new_serial.data)
        return Response(new_serial.data, status=status.HTTP_201_CREATED)
    return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return Response({"error": "Question not found"}, status=404)

    serializer = QuestionSerial(question)
    return Response(serializer.data)



@api_view(['GET'])
def get_all_questions(request):
    questions = Question.objects.annotate(
        good=Exists(
            Question.likes.through.objects.filter(
                question_id=OuterRef('id'),
                user=request.user
            )
        ),
    ).all()

    serializer = QuestionSerial(questions, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_answer(request):
    print(request.data)
    serializer = AddCommentSerial(data=request.data, context={"user": request.user})
    print(serializer.is_valid())
    print(serializer.errors)
    if serializer.is_valid():
        x = serializer.save()
        return Response(CommentSerial(x).data, status=201)
    return Response(serializer.errors, status=400)

# {
#     "comment": "The capital of France is Paris.",
#     "question_id": 1
# }


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    data = User.objects.get(id=request.user.id)
    serial = UserTestSerial(data)
    return Response({"user": serial.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def like_question(request):
    question = get_object_or_404(Question, id=request.data["id"])

    if question.likes.filter(id=request.user.id).exists():
        question.likes.remove(request.user)
    else:
        question.likes.add(request.user)

    question_annotated = Question.objects.filter(pk=question.id).annotate(
        good=Exists(
            Question.likes.through.objects.filter(
                question_id=OuterRef('pk'),
                user_id=request.user.id
            )
        ),
    ).first()

    serializer = QuestionSerial(question_annotated)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_answer(request):
    answer = get_object_or_404(Comment, id=request.data["id"])
    if answer.likes.filter(id=request.user.id).exists():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)

    answer_annotated = Comment.objects.filter(pk=answer.id).annotate(
        good=Exists(
            Comment.likes.through.objects.filter(
                comment_id=OuterRef('id'),
                user_id=request.user.id
            )
        ),
    ).first()

    serializer = CommentSerial(answer_annotated)
    return Response(serializer.data, status=200)



@api_view(['GET'])
def get_all_category(request):
    categories = Category.objects.all()
    serializer = CategorySerial(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def log_out(request):
    try:
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


