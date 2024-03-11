# main_script.py

import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a Schoolsafe and kind AI Assistant."},
]

blacklist = ["essay", "evaluate", "solve"]

def is_blacklisted(text):
    return any(word in text.lower() for word in blacklist)

def Blacklist_Reply():
    # Blacklisted word said
    script = """
        Sorry I cant respond to that as that is against policies or I dont understand that. Try checking your grammar and spelling!
    """
    return script

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        if is_blacklisted(input):
            # Instead of responding, delete text boxes
            return Blacklist_Reply()
        else:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply if not is_blacklisted(reply) else Blacklist_Reply()

# Gradio Interface Setup:
inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="SchoolSafe",
             description="School safe AI chatbot ",
             theme="compact").launch(share=True)
