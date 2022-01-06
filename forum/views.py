from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import MessageSerializer, ThemeSerializer, ThreadSerializer
from .models import Message, Thread, Theme
from users.models import User
import jwt

# Create your views here.
class CreateMessage(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = payload['id']
        theme = request.data['theme_id']
        text = request.data['text']

        msg = Message.objects.create(user_id=user, theme_id=theme, text=text)

        serializer = MessageSerializer(msg)
        return Response(serializer.data)

class CreateTheme(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = payload['id']
        thread = request.data['thread_id']
        title = request.data['title']
        text = request.data['text']

        theme = Theme.objects.create(user_id=user, thread_id=thread, title=title, text=text)

        serializer = ThemeSerializer(theme)
        return Response(serializer.data)

class CreateThread(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.filter(id=payload['id']).first()
        print(user.is_staff)
        if not user.is_staff:
            return Response({'AccessDenied': 'not admin'})
        
        title = request.data['title']

        thread = Thread.objects.create(title=title)

        serializer = ThreadSerializer(thread)

        return Response(serializer.data)
