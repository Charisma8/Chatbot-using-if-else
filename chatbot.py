
def chatbot():
    user_name = ""  
    print(" Hello! I'm your advanced chatbot.")
    print(" I can do math, tell jokes, remember your name, and much more!")
    print(" Try saying: 'my name is [your name]' or '5 + 3' or 'tell me a joke'")
    print("-" * 60)
    
    while True:
        user_input = input("\nYou: ").lower().strip()
        
        # Exit commands
        if user_input in ["bye", "quit", "exit", "goodbye"]:
            if user_name:
                print(f" Goodbye {user_name}! Have a great day! ")
            else:
                print(" Goodbye! Have a great day! ")
            break
        
        # Greetings
        elif user_input in ["hello", "hi", "hey", "greetings"]:
            if user_name:
                print(f"🤖 Hello {user_name}! How can I help you today?")
            else:
                print(" Hello there! How can I help you today?")
        
        # How are you responses
        elif "how are you" in user_input or "how do you do" in user_input:
            print(" I'm doing great! Thanks for asking. How are you?")
        
        # Name learning - when user tells their name
        elif "my name is" in user_input:
            user_name = user_input.replace("my name is", "").strip().title()
            print(f" Nice to meet you, {user_name}! I'll remember that.")
        
        # Name recall - when user asks what their name is
        elif user_name and ("what is my name" in user_input or "my name" in user_input):
            print(f" Your name is {user_name}!")
        
        # Bot name questions
        elif "your name" in user_input or "who are you" in user_input:
            print(" I'm an advanced chatbot created to help and chat with you!")
        
        # Time questions
        elif "time" in user_input:
            import datetime
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f" The current time is {current_time}")
        
        # Date questions
        elif "date" in user_input or "today" in user_input:
            import datetime
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f" Today is {current_date}")
        
        # Multiple jokes with random selection
        elif "joke" in user_input or "funny" in user_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call a fake noodle? An impasta!",
                "Why did the math book look sad? Because it was full of problems!",
                "What do you call a bear with no teeth? A gummy bear!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a sleeping bull? A bulldozer!",
                "Why did the computer go to the doctor? Because it had a virus!"
            ]
            import random
            print(f" {random.choice(jokes)}")
        
        # Simple math - Addition
        elif "+" in user_input:
            try:
                parts = user_input.split("+")
                if len(parts) == 2:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    result = num1 + num2
                    print(f" {num1} + {num2} = {result}")
                else:
                    print(" Please use format like: 5 + 3")
            except:
                print(" I couldn't solve that math problem. Try something like: 5 + 3")
        
        # Simple math - Subtraction
        elif "-" in user_input and not user_input.startswith("-"):
            try:
                parts = user_input.split("-")
                if len(parts) == 2:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    result = num1 - num2
                    print(f" {num1} - {num2} = {result}")
                else:
                    print(" Please use format like: 10 - 3")
            except:
                print(" I couldn't solve that math problem. Try something like: 10 - 3")
        
        # Simple math - Multiplication
        elif "*" in user_input or "x" in user_input:
            try:
                if "*" in user_input:
                    parts = user_input.split("*")
                else:
                    parts = user_input.split("x")
                if len(parts) == 2:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    result = num1 * num2
                    print(f" {num1} × {num2} = {result}")
                else:
                    print(" Please use format like: 5 * 3 or 5 x 3")
            except:
                print(" I couldn't solve that math problem. Try something like: 5 * 3")
        
        # Weather questions
        elif "weather" in user_input:
            print(" I don't have access to real weather data, but I hope it's nice where you are!")
        
        # Age questions
        elif "age" in user_input or "old are you" in user_input:
            print(" I'm a computer program, so I don't really have an age! But I was just created today.")
        
        # Help requests
        elif "help" in user_input:
            print(" I can help you with many things!")
            print(" Try asking me about: time, date, weather, jokes, math, or just chat!")
            print(" You can also tell me your name by saying 'my name is [your name]'")
        
        # Thank you responses
        elif "thank you" in user_input or "thanks" in user_input:
            print(" You're very welcome! Happy to help! 😊")
        
        # Compliments
        elif "good" in user_input or "great" in user_input or "awesome" in user_input:
            print(" Thank you! That's very kind of you to say!")
        
        # Favorite things
        elif "favorite color" in user_input:
            print(" I like blue! It reminds me of the digital world. What's your favorite color?")
        
        elif "favorite food" in user_input:
            print(" I don't eat food, but if I could, I think I'd like pizza! What's your favorite?")
        
        # Empty input
        elif user_input == "":
            print(" I didn't hear anything. Could you please say something?")
        
        # Default responses with variety
        else:
            responses = [
                "That's interesting! Tell me more.",
                "I'm not sure I understand. Could you rephrase that?",
                "Hmm, I don't know much about that topic yet.",
                "That's a good point! What else would you like to talk about?",
                "I'm still learning! Is there something else I can help you with?",
                "That sounds fascinating! Can you explain more?",
                "I'd love to learn about that! Tell me more."
            ]
            import random
            print(f" {random.choice(responses)}")

# Start the chatbot
if __name__ == "__main__":
    chatbot()
