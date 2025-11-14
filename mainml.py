# Program chatbot ini termasuk Machine Learning.
# Program chatbot ini menggunakan algoritma Machine Learning Multinomial Naive Bayes.

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Load knowledge_base.json
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

knowledge_base = load_knowledge_base("knowledge_base.json")

# 2. Siapkan dataset dari knowledge_base
questions = [q["question"] for q in knowledge_base["questions"]]
answers = [q["answer"] for q in knowledge_base["questions"]]

# Untuk intent sederhana, kita pakai index pertanyaan sebagai label
intents = [str(i) for i in range(len(questions))]

# 3. Vectorizer + Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = MultinomialNB()
model.fit(X, intents)

# 4. Fungsi chatbot
def chat_bot():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        X_test = vectorizer.transform([user_input])
        predicted_intent = model.predict(X_test)[0]

        # Ambil jawaban sesuai intent
        answer = answers[int(predicted_intent)]
        print(f"Bot: {answer}")

if __name__ == "__main__":
    chat_bot()