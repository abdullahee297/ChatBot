import requests
import json
from django.shortcuts import render
from django.http import StreamingHttpResponse

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