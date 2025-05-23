import time
import random

# --- User Class ---
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# --- Question Class ---
class Question:
    def __init__(self, prompt_en, prompt_fr, options_en, options_fr, correct_option, category):
        self.prompt_en = prompt_en
        self.prompt_fr = prompt_fr
        self.options_en = options_en
        self.options_fr = options_fr
        self.correct_option = correct_option.upper()
        self.category = category

    def is_correct(self, answer):
        return answer.upper() == self.correct_option

    def display(self, lang="en"):
        print(f"\n📘 Category: {self.category}")
        print(self.prompt_en if lang == "en" else self.prompt_fr)
        options = self.options_en if lang == "en" else self.options_fr
        for key, value in options.items():
            print(f"  {key}. {value}")


# --- Quiz Class ---
class Quiz:
    def __init__(self, user, questions, language="en", time_limit=30):
        self.user = user
        self.questions = questions
        random.shuffle(self.questions)
        self.language = language
        self.time_limit = time_limit
        self.score = 0

    def run(self):
        print(f"\n🚗 Welcome, {self.user.name}! Starting the driving license quiz.")
        print(f"🕒 Time limit per question: {self.time_limit} seconds\n")

        for index, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}/{len(self.questions)}:")
            question.display(self.language)

            start_time = time.time()
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            time_taken = time.time() - start_time

            if time_taken > self.time_limit:
                print(f"⏰ Time's up! You took {int(time_taken)} seconds.")
                continue

            if question.is_correct(answer):
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Incorrect. Correct answer was: {question.correct_option}")

        self.display_result()

    def display_result(self):
        print(f"\n🎓 Final Score: {self.score}/{len(self.questions)}")
        percent = (self.score / len(self.questions)) * 100
        print(f"📊 Result: {percent:.1f}%")
        if percent >= 70:
            print("🎉 PASS – You qualified for your driving license!")
        else:
            print("❌ FAIL – Better luck next time.")
            # Save to file
        # with open("quiz_results.txt", "a") as file:
        # file.write(f"{self.user.name}, Age: {self.user.age}, Score: {self.score}/{len(self.questions)}, "
        # f"Percent: {percent:.1f}%, Language: {self.language}, Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

# --- Define Questions ---
questions = [
    Question("What does a red traffic light mean?", "Que signifie un feu rouge ?",
             {"A": "Go", "B": "Stop", "C": "Slow down", "D": "Turn left"},
             {"A": "Avancer", "B": "Arrêter", "C": "Ralentir", "D": "Tourner à gauche"},
             "B", "Traffic Lights"),
    Question("When is it legal to use a mobile phone while driving?", "Quand est-il légal d'utiliser un téléphone au volant ?",
             {"A": "Hands-free", "B": "At red light", "C": "Never", "D": "While driving slowly"},
             {"A": "Kit mains libres", "B": "Au feu rouge", "C": "Jamais", "D": "En roulant doucement"},
             "A", "Rules"),
    Question("What must you do at a stop sign?", "Que faire à un panneau STOP ?",
             {"A": "Slow down", "B": "Stop if traffic", "C": "Full stop", "D": "Honk"},
             {"A": "Ralentir", "B": "Arrêter s’il y a du trafic", "C": "S'arrêter", "D": "Klaxonner"},
             "C", "Signs"),
    Question("Minimum tread depth on a tire?", "Profondeur minimale de bande de roulement ?",
             {"A": "1.0 mm", "B": "1.6 mm", "C": "2.0 mm", "D": "2.5 mm"},
             {"A": "1.0 mm", "B": "1.6 mm", "C": "2.0 mm", "D": "2.5 mm"},
             "B", "Vehicle Safety"),
    Question("Yellow diamond sign indicates?", "Un panneau jaune en losange signifie ?",
             {"A": "Yield", "B": "Warning", "C": "Regulatory", "D": "Direction"},
             {"A": "Cédez", "B": "Avertissement", "C": "Réglementation", "D": "Direction"},
             "B", "Signs"),
    Question("When should headlights be used?", "Quand utiliser les phares ?",
             {"A": "Before sunset", "B": "Low visibility", "C": "Night", "D": "All of the above"},
             {"A": "Avant le coucher du soleil", "B": "Faible visibilité", "C": "Nuit", "D": "Tout ce qui précède"},
             "D", "Vehicle Control"),
    Question("Breakdown on motorway?", "Panne sur l'autoroute ?",
             {"A": "Push vehicle", "B": "Stay inside", "C": "Use hazard lights", "D": "Exit and wait"},
             {"A": "Pousser", "B": "Rester dedans", "C": "Feux de détresse", "D": "Sortir"},
             "C", "Emergency Procedures"),
    Question("Flashing amber at crossing means?", "Feu orange clignotant signifie ?",
             {"A": "Go", "B": "Stop", "C": "Give way", "D": "Wait for green"},
             {"A": "Avancer", "B": "Stop", "C": "Cédez", "D": "Attendez le vert"},
             "C", "Pedestrian Crossings"),
    Question("Speed limit on dual carriageway?", "Limite sur voie rapide ?",
             {"A": "30", "B": "50", "C": "60", "D": "70"},
             {"A": "30", "B": "50", "C": "60", "D": "70"},
             "D", "Speed Limits"),
    Question("At roundabouts, you must?", "À un rond-point, vous devez ?",
             {"A": "Speed up", "B": "Yield right", "C": "Stop", "D": "Signal left"},
             {"A": "Accélérer", "B": "Céder à droite", "C": "Stop", "D": "Clignotant gauche"},
             "B", "Road Rules"),
    Question("Chevron markings indicate?", "Marquage en chevrons ?",
             {"A": "Bus lane", "B": "Guidance", "C": "No overtaking", "D": "Crosswalk"},
             {"A": "Voie bus", "B": "Guidage", "C": "Interdit dépasser", "D": "Passage piétons"},
             "C", "Road Markings"),
    Question("Safe overtaking condition?", "Quand dépasser ?",
             {"A": "On bend", "B": "At crossing", "C": "Clear dual carriageway", "D": "If front stops"},
             {"A": "Dans virage", "B": "Passage piétons", "C": "Voie dégagée", "D": "Si arrêt devant"},
             "C", "Safe Driving"),
    Question("Blue circle road sign means?", "Cercle bleu signifie ?",
             {"A": "Prohibition", "B": "Information", "C": "Mandatory", "D": "Warning"},
             {"A": "Interdiction", "B": "Information", "C": "Obligatoire", "D": "Avertissement"},
             "C", "Signs"),
    Question("Flashing red on school bus means?", "Feux rouges clignotants sur bus scolaire ?",
             {"A": "Drive normal", "B": "Stop", "C": "Overtake", "D": "Honk"},
             {"A": "Normal", "B": "Arrêter", "C": "Doubler", "D": "Klaxonner"},
             "B", "School Zones"),
    Question("Purpose of ABS?", "Fonction de l’ABS ?",
             {"A": "Longer brakes", "B": "Prevent lock", "C": "Fuel saving", "D": "More power"},
             {"A": "Frein long", "B": "Empêcher blocage", "C": "Économie", "D": "Plus puissant"},
             "B", "Vehicle Safety"),
    Question("Triangle sign with red border means?", "Triangle rouge signifie ?",
             {"A": "Warning", "B": "Yield", "C": "Stop", "D": "No entry"},
             {"A": "Avertissement", "B": "Cédez", "C": "Stop", "D": "Sens interdit"},
             "A", "Signs"),
    Question("When to use horn?", "Quand klaxonner ?",
             {"A": "Greet", "B": "Alert others", "C": "Frustration", "D": "Change lane"},
             {"A": "Saluer", "B": "Alerter", "C": "Frustré", "D": "Changer de voie"},
             "B", "Driving Etiquette"),
    Question("Green light means?", "Feu vert signifie ?",
             {"A": "Stop", "B": "Go", "C": "Yield", "D": "Prepare"},
             {"A": "Arrêt", "B": "Avancer", "C": "Cédez", "D": "Préparez"},
             "B", "Traffic Lights"),
    Question("Miss exit on motorway?", "Sortie manquée ?",
             {"A": "Reverse", "B": "Next exit", "C": "Stop", "D": "U-turn"},
             {"A": "Reculer", "B": "Prochaine sortie", "C": "Arrêter", "D": "Faire demi-tour"},
             "B", "Motorway Rules"),
    Question("Legal BAC limit for drivers?", "Taux légal d’alcoolémie ?",
             {"A": "0.02%", "B": "0.05%", "C": "0.08%", "D": "0.10%"},
             {"A": "0.02%", "B": "0.05%", "C": "0.08%", "D": "0.10%"},
             "C", "Alcohol & Driving")
]

# --- Main Program ---
def main():
    print("👤 Welcome to the Driving License Quiz!")
    name = input("Enter your name: ")
    
    age_input = input("Enter your age: ")
    if not age_input.isdigit():
        print("⚠️ Please enter a valid age.")
        return main()  # Restart if non-numeric input

    age = int(age_input)

    if age < 16:
        print("❌ You must be at least 16 years old to take the driving license quiz.")
        time.sleep(2)
        return main()  # Bring back to main menu

    user = User(name, age)

    print("\n🌍 Choose your language / Choisissez votre langue:")
    print("1. English\n2. Français")
    lang_choice = input("Your choice: ")
    language = "fr" if lang_choice == "2" else "en"

    quiz = Quiz(user, questions, language=language, time_limit = 30)
    quiz.run()

#Run it
main()
