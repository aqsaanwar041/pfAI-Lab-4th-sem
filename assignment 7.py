symptoms_list = [
    "fever", "cough", "headache", "fatigue",
    "runny nose", "sore throat", "body pain", "vomiting"
]

rules = {
    "flu": ["fever", "cough", "headache", "fatigue"],
    "cold": ["runny nose", "cough", "sore throat"],
    "infection": ["fever", "body pain", "vomiting"],
    "migraine": ["headache", "fatigue"]
}

def diagnose(symptoms_given):
    possible_diseases = []
    for disease, rule_symptoms in rules.items():
        match_count = 0
        for s in symptoms_given:
            if s in rule_symptoms:
                match_count += 1
        if match_count >= len(rule_symptoms) / 2:
            possible_diseases.append(disease)
    return possible_diseases

def ask_user():
    print("\n------------------------------")
    print("   MEDICAL EXPERT SYSTEM")
    print("------------------------------\n")
    print("Enter your symptoms (comma separated). Example: fever, cough")
    
    symptoms_input = input("Symptoms: ")
    user_symptoms = [s.strip().lower() for s in symptoms_input.split(",")]
    result = diagnose(user_symptoms)

    print("\n------------------------------")
    print("           RESULT")
    print("------------------------------")

    if len(result) == 0:
        print("No disease found matching your symptoms.")
    else:
        print("Possible Diseases:")
        for d in result:
            print(" -", d)

    print("\n------------------------------")

ask_user()

