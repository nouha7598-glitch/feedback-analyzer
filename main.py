import string

positive_words = ["good", "great", "excellent", "happy", "love", "amazing", "awesome", "nice"]
negative_words = ["bad", "poor", "terrible", "hate", "sad", "awful", "horrible", "disgusting"]

def analyze_feedback(text):
    score = 0
    
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        return "Positive 😊"
    elif score < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"


print("📊 Feedback Analyzer Started!")

while True:
    feedback = input("\nEnter feedback (or 'exit'): ")

    if feedback.lower() == "exit":
        print("Goodbye 👋")
        break

    result = analyze_feedback(feedback)
    print("Result:", result)
