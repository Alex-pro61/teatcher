import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import openai
import requests

# API ключ для ChatGPT
openai.api_key = "your_openai_api_key"  # Замість цього додайте ключ до .env і використовуйте os.getenv

st.title("Віртуальний Вчитель")
st.subheader("Вікно Учня")

# Відображення відео з веб-камери
class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame  # Повертає оригінальний кадр без змін

webrtc_streamer(key="example", video_processor_factory=VideoProcessor)

# Поле для вводу тексту
st.subheader("Чат з Віртуальним Вчителем")
user_input = st.text_input("Введіть ваше запитання до вчителя:", "")

if st.button("Надіслати"):
    if user_input.strip():
        # Отримання відповіді від ChatGPT
        with st.spinner("Генерується відповідь..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}],
                )
                reply = response['choices'][0]['message']['content']
                st.text_area("Відповідь Віртуального Вчителя:", reply, height=200)
            except Exception as e:
                st.error(f"Сталася помилка: {e}")
    else:
        st.warning("Будь ласка, введіть текст для надсилання.")

# Додаткове поле для титрів
st.subheader("Титри")
show_captions = st.checkbox("Показати титри", value=True)

if show_captions:
    st.text("Тут з’являться титри в майбутньому.")

