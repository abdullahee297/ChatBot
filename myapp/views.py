import requests
import json
import speech_recognition as sr
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from tkinter import *
import speech_recognition as sr

recognizer = sr.Recognizer()



OLLAMA_URL = "http://localhost:11434/api/generate"

def ollama_stream(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": True
    }

    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            chunk = data.get("response", "")
            yield chunk

def chatbot(request):
    if request.method == "GET":
        request.session["messages"] = []

    return render(request, "index.html", {
        "messages": request.session["messages"]
    })



# def micbtn():
#     text = record_text()
#     messages = request.session.get("messages", [])
#     messages.append({"type": "user", "text": text})


def chatbot_stream(request):
    prompt = request.GET.get("prompt", "")

    if not prompt:
        return StreamingHttpResponse("No prompt provided", content_type="text/plain")

    def generate():
        full_response = ""

        for chunk in ollama_stream(prompt):
            full_response += chunk
            yield chunk
        
        messages = request.session.get("messages", [])

        messages.append({"type": "user", "text": prompt})
        messages.append({"type": "bot", "text": full_response})

        request.session["messages"] = messages

    return StreamingHttpResponse(generate(), content_type="text/plain")

def record_text():
    try:
        with sr.Microphone() as mic:
            # label.config(text="Listening...")
            # root.update()
            print("Listening....")

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            return text

    except sr.UnknownValueError:
        return "Could not understand"
    except sr.RequestError:
        return "API error"
    except Exception as e:
        return str(e)
    

from pydub import AudioSegment
import tempfile

def speech_to_text(request):
    if request.method == "POST" and request.FILES.get("audio"):
        audio_file = request.FILES["audio"]
        recognizer = sr.Recognizer()

        try:
            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_audio:
                for chunk in audio_file.chunks():
                    temp_audio.write(chunk)
                temp_audio_path = temp_audio.name

            # Convert to WAV
            sound = AudioSegment.from_file(temp_audio_path)
            wav_path = temp_audio_path.replace(".webm", ".wav")
            sound.export(wav_path, format="wav")

            # Read WAV
            with sr.AudioFile(wav_path) as source:
                audio = recognizer.record(source)

            text = recognizer.recognize_google(audio)

            return JsonResponse({"text": text})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"})
