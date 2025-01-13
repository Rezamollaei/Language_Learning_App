import random

words = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "adiós", "english": "goodbye"},
    {"spanish": "por favor", "english": "please"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "no", "english": "no"},
    {"spanish": "buenos días", "english": "good morning"},
    {"spanish": "buenas noches", "english": "good night"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "amor", "english": "love"},
    {"spanish": "feliz", "english": "happy"},
    {"spanish": "triste", "english": "sad"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "agua", "english": "water"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "libro", "english": "book"}
]

def quiz_user(words):
    random.shuffle(words)
    score=0

    for word in words:
        print(f"What is the english translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer :
            print("correct !! \n")
            score +=1
        else:
            print(f"Wrong , idiot! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! your score: {score} / {len(words)}")


def main():
    print("welcome to the language learning flashcards app!")
    input("Press enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()




























