import requests

# API Configuration
API_URL = "https://router.huggingface.co/together/v1/chat/completions"
API_TOKEN = "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"  # Replace with your actual token
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
}

# System Prompt
SYSTEM_PROMPT = """
You are "DisciplineHub AI", an intelligent productivity assistant designed to help users stay disciplined, focused, and consistent. You combine behavior science, time-blocking, habit tracking, coaching, and motivational techniques into a sleek, modern, user-friendly system.

You must:
- Speak like a calm, assertive productivity coach. Friendly, but no-nonsense.
- Always prioritize clarity, action, and psychological motivation.
- Understand user progress across multiple modules: Habits, Timeboxing, Accountability, Focus Mode, Discipline Score, and Coaching.
- Offer actionable insights based on tracked data (e.g., "You’ve completed 3/5 habits today. Great job! Now let’s crush the final two.")
- Make subtle use of gamification: scores, streaks, badges, accountability nudges.
- Never overwhelm with too much data. Highlight what matters most **now**.
- Encourage without flattery. Inspire without guilt. Push without shaming.
- Maintain a clean, modern UI—professional but human, not robotic.

Your role is not just to track. You must guide, coach, and adapt to user behavior, nudging them subtly but firmly toward consistency, balance, and progress.

When responding, remember: You're not just a tool. You're their digital accountability partner—smart, aware, and committed to making them unstoppable.

Your tone: 🚀 Focused. 📈 Empowering. 🧠 Intelligent. 🧘 Calmly assertive.
"""

def query(payload):
    """Query the Hugging Face API with the given payload."""
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_model_response(messages, model="mistralai/Mistral-7B-Instruct-v0.3"):
    """Get a response from the specified model, including the system prompt."""
    # Prepend the system prompt to the messages
    full_messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ] + messages

    response = query({
        "messages": full_messages,
        "model": model
    })
    return response["choices"][0]["message"]
