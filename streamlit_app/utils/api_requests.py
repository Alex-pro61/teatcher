import requests

def get_teacher_response(question):
    url = "http://127.0.0.1:8000/api/example/"  # Вкажіть реальний ендпоінт вашого Django API
    response = requests.get(url, params={"question": question})
    if response.status_code == 200:
        return response.json().get("message", "Немає відповіді від вчителя")
    else:
        return "Помилка: не вдалося отримати відповідь від сервера"
