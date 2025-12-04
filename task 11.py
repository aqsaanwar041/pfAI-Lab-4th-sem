from transformers import pipeline
chatbot = pipeline("text-generation", model="gpt2")
response = chatbot("Hello, I'm a chatbot built with Hugging Face!", max_length=50, do_sample=True)
print(response[0]['generated_text'])
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Bye!")
        break
    response = chatbot(user_input, max_length=50, do_sample=True)
    print("Chatbot:", response[0]['generated_text'])
