from django.contrib.auth.models import User
from django.db.models import Exists, OuterRef
from rest_framework import serializers
from .models import Category, Question, Comment


class UserTestSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "email","password1","password2"]


class CategorySerial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerial(serializers.ModelSerializer):
    user = UserTestSerial(read_only=True, allow_null=True)
    good = serializers.BooleanField(allow_null=True)
    likes = serializers.IntegerField(source="likes.count")

    def create(self, data):
        print("Serial", data)
        return Comment.objects.create(**data)

    def get_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'question_id', 'likes', 'good', 'user']



class AddCommentSerial(serializers.ModelSerializer):
    user = UserTestSerial(read_only=True, allow_null=True)
    def create(self, data):
        print("Serial", data)
        print("user", self.context["user"])
        return Comment.objects.create(**data, user=self.context["user"] )

    class Meta:
        model = Comment
        fields = ['comment', 'question_id', 'user']



class QuestionSerial(serializers.ModelSerializer):
    comments = CommentSerial(many=True, read_only=True)
    category = CategorySerial()
    user = UserTestSerial(read_only=True)
    good = serializers.BooleanField(allow_null=True)
    # like_count = serializers.IntegerField(read_only=True)
    likes = serializers.IntegerField(source="likes.count")

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get_or_create(**category_data)[0]
        question = Question.objects.create(category=category, **validated_data)
        return question


    def get_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Question
        fields = ['id', 'question', 'category', 'user', 'good', 'likes', 'comments']








class AddQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question", "category"]
    def create(self, data):
            user = self.context['user']
            question = Question.objects.create(user=self.context["user"], **data)
            return question



    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     category, created = Category.objects.get_or_create(**category_data)
    #     question = Question.objects.create(category=category, **validated_data)
    #     return question



