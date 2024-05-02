import os
from gtts import gTTS
from playsound import playsound
import re

def read_text_from_file(file_path):
    # Проверяем, существует ли указанный файл
    if not os.path.exists(file_path):
        print("Указанный файл не существует.")
        return None

    # Открываем файл для чтения
    with open(file_path, 'r', encoding='utf-8') as file:
        # Читаем текст из файла
        text = file.read()
    return text


def split_into_sentences(text):
    # Разделение строки на предложения по знакам пунктуации, которые часто являются концами предложений
    sentences = re.split(r'(?<!\w\.\w.)(?<![А-Яа-яЁё]\.)(?<=\.|\?|\!)\s', text)
    # Удаление пустых элементов (возможно, после последнего предложения)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences


def text_to_speech(text, file_path):
    # Озвучиваем текст
    tts = gTTS(text=text, lang='ru')
    # Сохраняем аудиофайл
    tts.save(file_path)
    print(f"Аудиофайл сохранен как {file_path}")

    playsound(file_path)

# Пример использования функции
file_path = 'input.txt'
text = read_text_from_file(file_path)

sentences = split_into_sentences(text)

print("Отдельные предложения:")

for i, sentence in enumerate(sentences):
    print(f"Предложение {i+1}: {sentence}")
    text_to_speech(sentence, f"audio{i + 1}.mp3")

