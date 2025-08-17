import google.generativeai as genai

# Your Gemini API Key
GEMINI_API_KEY = "AIzaSyD1sNVmx5d7MFCbcWU9xXxsQ43kHCAxt-c"
genai.configure(api_key=GEMINI_API_KEY)

# Create the model (use the updated name)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def completion(user_input):
    response = chat.send_message(user_input)
    print(f"Jarvis: {response.text}")

if __name__ == "__main__":
    print("Jarvis: Hi I am Jarvis, How may I help you?\n")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Jarvis: Goodbye!")
            break
        completion(user_input)
