import os
import json
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key="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")

def groq_stream(prompt):
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=True
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content


def chatbot(request):
    if request.method == "GET":
        request.session["messages"] = []

    return render(request, "index.html", {
        "messages": request.session.get("messages", [])
    })


def chatbot_stream(request):
    prompt = request.GET.get("prompt", "")

    if not prompt:
        return StreamingHttpResponse("No prompt provided", content_type="text/plain")

    def generate():
        try:
            full_response = ""

            for chunk in groq_stream(prompt):
                full_response += chunk
                yield chunk

            # Save chat history
            messages = request.session.get("messages", [])
            messages.append({"type": "user", "text": prompt})
            messages.append({"type": "bot", "text": full_response})
            request.session["messages"] = messages

        except Exception as e:
            yield f"\nError: {str(e)}"

    return StreamingHttpResponse(generate(), content_type="text/plain")
