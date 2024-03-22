from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from g4f.client import Client
import g4f

class ChatView(APIView):
    def get(self, request):
        return render(request, 'chat.html',{'display_message': "Hello, I'm here to help you"})
    def post(self, request):
        MODEL = g4f.models.airoboros_70b
        PROVIDER=g4f.Provider.DeepInfra

        question = request.data.get("question",None)
        if question:
            client = Client()
            response = client.chat.completions.create(
                model=MODEL,
                provider=PROVIDER,
                messages=[{"role": "user", "content": f"{question}"}])
            bot_response = response.choices[0].message.content
            return render(request, 'chat.html', {'question': question, 'bot_response': bot_response})
        else:
            return render(request, 'chat.html', {'error_message': 'Data Insufficient'})
                
