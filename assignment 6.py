

def diagnose(symptoms):
    if "fever" in symptoms and "cough" in symptoms and "headache" in symptoms:
        return "Flu"
    elif "cough" in symptoms and "sore throat" in symptoms:
        return "Common Cold"
    elif "fever" in symptoms and "sore throat" in symptoms:
        return "Throat Infection"
    else:
        return "Unknown Disease"

def is_sentence(words):
    nouns = ["cat", "dog", "boy", "girl"]
    verbs = ["runs", "eats", "sees"]

    if len(words) == 2 and words[0] in nouns and words[1] in verbs:
        return True
    return False

print("===== SIMPLE AI SYSTEM =====")
print("1. Medical Expert System")
print("2. Sentence Checker (NLP)")
print("3. Face Detection (OpenCV)")
choice = input("Choose option (1/2/3): ")
if choice == "1":
    print("\nEnter symptoms (comma separated):")
    user_input = input("Symptoms: ").lower().split(",")
    symptoms = [x.strip() for x in user_input]

    print("Diagnosis:", diagnose(symptoms))
elif choice == "2":
    sentence = input("\nEnter 2-word sentence (e.g., dog runs): ").lower().split()
    if is_sentence(sentence):
        print("Valid Sentence ✔")
    else:
        print("Invalid Sentence ❌")
elif choice == "3":
    print("\nStarting Face Detection... Press Q to quit.")

    import cv2
    face = cv2.CascadeClassifier(cv2.data.haarcascades +
                                 "haarcascade_frontalface_default.xml")

    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

else:
    print("Invalid option!")
