import csv
import json  # Import the JSON module for handling JSON data
import os  # Import the OS module for interacting with the operating system
import time  # Import time module for retry logic
from ai21 import AI21Client  # Import the AI21Client class for interacting with the AI21 API
from ai21.models.chat import UserMessage  # Import UserMessage class for structuring chat messages
from deep_translator import GoogleTranslator  # Import GoogleTranslator for translation services
from langdetect import detect  # Import detect function for language detection
import logging  # Import the logging module for logging messages
import pandas as pd
import glob
import csv

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

file1=open("home_drilled.csv","r",encoding="utf8")
file2=open("High_drilled.csv","r",encoding="utf8")


# List of API key to use
api_key = [
    "78Qlsf3v7nK7nWydYBGPtxiYDc4S1Qfm","9XNOrcQ3GniqixX0vFxWSU0UkoGsiDR2","UFWaXmTqereBBCGVgwPgFa0UZ2Z6lyKl","ddNsbeF3vObrwSxeFbIyUgyPPq7OJM3L","pTBVfbDQ0G2cxqkhCYuDwFcULj4E6l6e"
]

# Initialize AI21Client with the first API key
client = AI21Client(api_key=api_key[0])
current_key_index = 0  # Track which API key is currently in use

# File to store conversation history
HISTORY_FILE = "conversation_history.json"

# Load conversation history from the file if it exists
if os.path.exists(HISTORY_FILE):
    try:
        with open(HISTORY_FILE, "r") as file:
            conversation_history = json.load(file)
        logging.info("Conversation history loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load conversation history: {e}")
        conversation_history = []  # Start fresh if loading fails
else:
    conversation_history = []  # Initialize an empty list if the file does not exist

# User profile with default values
user_profile = {
    "languages": ["English", "Hindi","Punjabi","Urdu","Bengali","Tamil","Telugu","Malayalam","Kannada","Gujarati","Marathi","Nepali"],  # Supported languages
    "preferred_language": "English",  # Default preferred language
    "preferences": {},  # Empty dictionary for user preferences
    "frequent_queries": []  # Empty list for storing frequent queries
}

def translate_to_user_language(user_input, ai_response):
    """Ensures the AI response is in the same language as the user input."""
    try:
        detected_language = detect(user_input)
        
        # Update preferred language if detected language is supported
        if detected_language == 'hi':
            user_profile["preferred_language"] = "Hindi"
        elif detected_language == 'en':
            user_profile["preferred_language"] = "English"
        elif detected_language=='bn':
            user_profile["preferred_language"]="Bengali"
        elif detected_language=='ta':
            user_profile["preferred_language"]="Tamil"
        elif detected_language=='te':
            user_profile["preferred_language"]="Telugu"
        elif detected_language=='ml':
            user_profile["preferred_language"]="Malayalam"
        elif detected_language=='kn':
            user_profile["preferred_language"]="Kannada"
        elif detected_language=='gu':
            user_profile["preferred_language"]="Gujarati"
        elif detected_language=='mr':
            user_profile["preferred_language"]="Marathi"
        elif detected_language=='pa':
            user_profile["preferred_language"]="Punjabi"
        elif detected_language=='ur':
            user_profile["preferred_language"]="Urdu"
        elif detected_language=='ne':
            user_profile["preferred_language"]="Nepali"
        
        # Translate AI response if preferred language is Hindi
        if user_profile["preferred_language"] == "Hindi":
            translated_response = GoogleTranslator(source='auto', target='hi').translate(ai_response)
            logging.info(f"Translated AI response from English to Hindi: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Bengali":
            translated_response = GoogleTranslator(source='auto', target='bn').translate(ai_response)
            logging.info(f"Translated AI response from English to Bengali: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Tamil":
            translated_response = GoogleTranslator(source='auto', target='ta').translate(ai_response)
            logging.info(f"Translated AI response from English to Tamil: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Telugu":
            translated_response = GoogleTranslator(source='auto', target='te').translate(ai_response)
            logging.info(f"Translated AI response from English to Telugu: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Malayalam":
            translated_response = GoogleTranslator(source='auto', target='ml').translate(ai_response)
            logging.info(f"Translated AI response from English to Malayalam: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Kannada":
            translated_response = GoogleTranslator(source='auto', target='kn').translate(ai_response)
            logging.info(f"Translated AI response from English to Kannada: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Gujarati":
            translated_response = GoogleTranslator(source='auto', target='gu').translate(ai_response)
            logging.info(f"Translated AI response from English to Gujarati: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Marathi":
            translated_response = GoogleTranslator(source='auto', target='mr').translate(ai_response)
            logging.info(f"Translated AI response from English to Marathi: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Punjabi":
            translated_response = GoogleTranslator(source='auto', target='pa').translate(ai_response)
            logging.info(f"Translated AI response from English to Punjabi: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Urdu":
            translated_response = GoogleTranslator(source='auto', target='ur').translate(ai_response)
            logging.info(f"Translated AI response from English to Urdu: {translated_response}")
            return translated_response
        elif user_profile["preferred_language"] == "Nepali":
            translated_response = GoogleTranslator(source='auto', target='ne').translate(ai_response)
            logging.info(f"Translated AI response from English to Nepali: {translated_response}")
            return translated_response
        else:
            return ai_response#in english as default
        
        
    except Exception as e:
        logging.error(f"Translation error: {e}")
        return f"Translation failed. Responding in original language: {ai_response}"


def save_conversation_history():
    """Saves the current conversation history to a file."""
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump(conversation_history, file)
        logging.info("Conversation history saved successfully.")
    except Exception as e:
        logging.error(f"Failed to save conversation history: {e}")
        # Consider implementing an in-memory backup or notifying the user of the issue

def is_valid_input(user_input):
    """Checks if the user input is not empty, just whitespace, or too long."""
    if not user_input.strip():
        return False
    if len(user_input) > 5000:  # Example limit
        logging.warning("Input too long")
        return False
    
    return True

def translate_to_english(user_input):
    """Translates user input to English if it's not already in English."""
    try:
        detected_language = detect(user_input)
        user_profile["language"] = detected_language
        if detected_language != 'en':
            translated_text = GoogleTranslator(source='auto', target='en').translate(user_input)
            logging.info(f"Translated '{user_input}' from {detected_language} to English: {translated_text}")
            return translated_text
        return user_input
    except Exception as e:
        logging.error(f"Translation error: {e}")
        return f"Translation failed. Responding in original language: {user_input}"

def estimate_max_tokens(user_input):
    """Estimates the maximum number of tokens based on the input length."""
    token_estimate = max(200, len(user_input) // 4)
    return min(token_estimate, 1000)

def split_large_query(user_input, max_length=1000):
    """Splits the user input into chunks if it exceeds the maximum length."""
    return [user_input[i:i+max_length] for i in range(0, len(user_input), max_length)]

def switch_api_key():
    """Switches to the next API key in the list."""
    global current_key_index, client
    current_key_index += 1
    if current_key_index < len(api_key):
        client = AI21Client(api_key=api_key[current_key_index])
        logging.info(f"Switched to API key {current_key_index + 1}.")
    else:
        logging.error("All API keys have been exhausted.")
        raise Exception("No more API keys available.")

def ai21_api_call(client, messages, retries=3):
    """Makes the API call to AI21, with retries if it fails."""
    attempt = 0
    while attempt < retries:
        try:
            response = client.chat.completions.create(
                model="jamba-1.5-large",
                messages=messages,
                top_p=0.9,
                temperature=0.5,
                max_tokens=estimate_max_tokens(messages[-1].content)
            )
            if response and response.choices and response.choices[0].message:
                return "\n" + response.choices[0].message.content.strip() + "\n"


        except Exception as e:
            logging.error(f"API call failed: {e}")
            attempt += 1
            time.sleep(2)  # Wait before retrying

            if "quota" in str(e).lower():
                logging.info("API quota exhausted. Attempting to switch API key.")
                try:
                    switch_api_key()
                except Exception as ex:
                    return str(ex)

    return "I'm having trouble connecting to my knowledge base right now. Please try again later."







def handle_user_input(user_input):
    """Handles the user input and generates a response using the CSV files or the AI21 API."""
    global conversation_history, user_profile  # Access global variables

    if not is_valid_input(user_input):
        return "Invalid input. Please provide a valid query."
    

    # Process specific queries for total data and high court data
    if "total data" in user_input.lower():
        r1 = home()
        r1 = validate_response(r1)  # Validate response from home()
        conversation_history.append((user_input, r1))  # Store in conversation history
        save_conversation_history()  # Save updated history
        logging.info(f"User Input: {user_input} | Response: {r1}")
        return r1

    elif "high court data" in user_input.lower():
        r2 = high()
        r2 = validate_response(r2)  # Validate response from high()
        conversation_history.append((user_input, r2))  # Store in conversation history
        save_conversation_history()  # Save updated history
        logging.info(f"User Input: {user_input} | Response: {r2}")
        return r2
    

    conversation_context = ""

    # Build the conversation context based on history
    for i, (prev_input, prev_response) in enumerate(conversation_history):
        conversation_context += f"User Query {i+1}: {prev_input}\nAI Response {i+1}: {prev_response}\n"

    conversation_context += f"User Query: {user_input}\n"

    try:
        max_tokens = estimate_max_tokens(user_input)

        if len(user_input) > 1000:
            parts = split_large_query(user_input)
            responses = []
            for part in parts:
                prompt = f'''
                You are NyayaSarthi, a Virtual Assistant for the Indian Department of Justice's Website. Below is a conversation history where the user asks questions related to the Indian Judiciary system. Use this history to provide an appropriate, precise, and concise response to the latest question only related to the Indian Judiciary. Do not answer mathematical questions. Answer greetings and only topic related to Indian Judiciary. While responding do not include the word NyayaSarthi unless asked who are you. Do not answer historical, philosophical, mathematical, scientific or geographic questions unless it is related to the Indian Judiciary.
                \n{conversation_context}
                User Query: {part}\n
                '''
                messages = [UserMessage(content=prompt)]
                output_text = ai21_api_call(client, messages)
                responses.append(output_text)

            final_response = "\n".join(responses)
            final_response = validate_response(final_response)

            conversation_history.append((user_input, final_response))
            save_conversation_history()

            logging.info(f"User Input: {user_input} | AI Response: {final_response}")
            return final_response

        prompt = f'''
        You are NyayaSarthi, a Virtual Assistant for the Indian Department of Justice's Website. Below is a conversation history where the user asks questions related to the Indian Judiciary system. Use this history to provide an appropriate, precise, and concise response to the latest question only related to the Indian Judiciary. Do not answer mathematical questions. Answer greetings and only topic related to Indian Judiciary. While responding do not include the word NyayaSarthi unless asked who are you. Do not answer historical, philosophical, mathematical, scientific or geographic questions unless it is related to the Indian Judiciary.
        \n{conversation_context}
        '''

        messages = [UserMessage(content=prompt)]
        output_text = ai21_api_call(client, messages)

        output_text = validate_response(output_text)

        if output_text == "The Indian Penal Code (IPC) includes several sections that are considered bailable offences...":
            return "I couldn't understand your query. Could you please clarify or ask a different question related to the Indian Judiciary system?"
        final_response = translate_to_user_language(user_input, output_text)

        conversation_history.append((user_input, final_response))
        save_conversation_history()

        logging.info(f"User Input: {user_input} | AI Response: {final_response}")
        return final_response

    except Exception as e:
        logging.error(f"Error while generating response: {e}")
        return "An unexpected error occurred. Please try again."



    
def validate_response(response_text):
    """Validates the response text to ensure it is relevant."""
    if not response_text or "The query is not related to the Indian Judiciary system." in response_text:
        return "I couldn't understand your query. Could you please clarify or ask a different question related to the Indian Judiciary system?"
    return response_text

def home():
    
    csv1=csv.DictReader(file1)
    for row1 in csv1:
        return row1
  
def high():
    
    csv2=csv.DictReader(file2)
    for row2 in csv2:
        return row2

file1.close()
file2.close()