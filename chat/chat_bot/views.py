from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from g4f.client import Client

class ChatView(APIView):
    def get(self, request):
        return render(request, 'chat.html',{'display_message': "Hello, I'm here to help you"})
    def post(self, request):
        question = request.data.get("question",None)
        if question:
            client = Client()
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": f"{question}"}])
            bot_response = response.choices[0].message.content
            return render(request, 'chat.html', {'question': question, 'bot_response': bot_response})
        else:
            return render(request, 'chat.html', {'error_message': 'Data Insufficient'})
                
