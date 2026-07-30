import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text


# Load FAQ data
with open("faq.json", "r") as file:
    faqs = json.load(file)


# Store questions and answers separately
questions = []
answers = []

for faq in faqs:
    questions.append(preprocess_text(faq["question"]))
    answers.append(faq["answer"])


# Convert questions into numerical form
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)


def get_answer(user_question):

    # Clean user question
    processed_question = preprocess_text(user_question)

    # Convert user question into vector
    user_vector = vectorizer.transform(
        [processed_question]
    )

    # Compare similarity
    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    # Find best matching question
    best_match = similarity.argmax()

    confidence = similarity[0][best_match]


    if confidence < 0.3:
        return "Sorry Bhumi, I could not understand your question."

    return answers[best_match]


# Start chatbot
if __name__ == "__main__":

    print("🤖 Bhumi's AI FAQ Chatbot")
    print("Type 'exit' to stop")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye Bhumi! 👋")
            break

        response = get_answer(user_input)

        print("Chatbot:", response)