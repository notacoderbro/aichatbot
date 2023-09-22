# chatbot.py
import re

def respond_to_query(query):
    query = query.lower()
    if "coal mines act" in query:
        return "The Coal Mines Act, 1952 is an important regulation for mining operations in India."
    elif "explosives act" in query:
        return "The Indian Explosives Act, 1884 governs the use of explosives in mining."
    elif "colliery control order" in query:
        return "The Colliery Control Order, 2000 lays down rules for the management of collieries."
    else:
        return "I'm sorry, I don't have information on that topic."

while True:
    user_input = input("You: ")
    response = respond_to_query(user_input)
    print("Chatbot:", response)
