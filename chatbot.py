import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq = {
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI.",
    "what is deep learning": "Deep Learning uses neural networks to learn patterns.",
    "what is python": "Python is a popular programming language.",
    "who developed python": "Python was developed by Guido van Rossum.",
    "what is data science": "Data Science is extracting useful insights from data.",
    "what is chatbot": "A chatbot is software that simulates human conversation.",
    "what is cloud computing": "Cloud computing provides services over the internet.",
    "what is nlp": "NLP helps computers understand human language.",
    "what is coding": "Coding is the process of writing computer programs."
}

questions = list(faq.keys())
answers = list(faq.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response():
    user_text = entry.get().lower().strip()

    if user_text == "":
        return

    chat_area.insert(tk.END, "You: " + user_text + "\n")

    user_vector = vectorizer.transform([user_text])
    similarity = cosine_similarity(user_vector, X)

    best_score = similarity.max()

    if best_score < 0.2:
        response = "Sorry, I don't know the answer to that question."
    else:
        index = similarity.argmax()
        response = answers[index]

    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    chat_area.see(tk.END)

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI FAQ Chatbot")
root.geometry("600x500")

title = tk.Label(root, text="AI FAQ Chatbot", font=("Arial", 16))
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(root, width=70, height=20)
chat_area.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=get_response)
send_button.pack(pady=5)

root.mainloop()