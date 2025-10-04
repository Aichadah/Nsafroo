from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")  # Ensure you have GROQ_API_KEY in your .env file
client = Groq(api_key=api_key)

app = Flask(__name__)

# System message to set chatbot behavior
system_message = {
    "role": "system",
    "content": "You are a helpful travel assistant. Your goal is to provide a suggestion of activities based on the budget and the destination, including the main activity the user wants to include."
}

# Function to generate activity suggestions using Groq API
def generate_suggestion(budget, currency, destination, activity):
    # Create a user message with the form data
    user_message = {
        "role": "user",
        "content": f"I am planning a trip to {destination} with a budget of {budget} {currency}. I want to include {activity} as the main activity. Can you suggest a detailed plan for my trip?"
    }

    # Send the message to the Groq API
    chat_completion = client.chat.completions.create(
        messages=[system_message, user_message],
        model="llama3-8b-8192",  # Use the appropriate model
    )

    # Extract the generated suggestion
    suggestion_text = chat_completion.choices[0].message.content

    # Structure the suggestion into sections
    suggestion = {
        "destination": destination,
        "budget": budget,
        "currency": currency,
        "activities": activity,
        "detailed_plan": suggestion_text,
    }
    return suggestion

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract form data
        budget = float(request.form['budget'])
        currency = request.form['currency']
        destination = request.form['destination']
        activity = request.form['activity']
        
        # Generate activity suggestion using Groq API
        suggestion = generate_suggestion(budget, currency, destination, activity)
        
        # Render the suggestion template with the result
        return render_template('suggestion.html', suggestion=suggestion)
    
    # Render the form template for GET requests
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
