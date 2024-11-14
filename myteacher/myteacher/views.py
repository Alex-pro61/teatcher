import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import ChatCompletion

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # Виклик API ChatGPT (налаштуйте згідно з вашим ключем і конфігурацією)
        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        chat_response = response.choices[0].message.content
        return JsonResponse({"reply": chat_response})
    return JsonResponse({"error": "Invalid request"}, status=400)
