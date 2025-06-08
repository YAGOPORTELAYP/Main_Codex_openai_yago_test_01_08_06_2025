import gradio as gr
from chatbot import ask_ollama

def respond(message, history):
    return ask_ollama(message)

demo = gr.ChatInterface(respond, title="Local Chatbot")

if __name__ == "__main__":
    demo.launch()
