
positive_words = ["good", "great", "excellent", "amazing", "love", "happy", "best"]
negative_words = ["bad", "sad", "hate", "terrible", "poor", "angry", "worst"]

while True:
    user_text = input("Enter a sentence or type exit to stop: ")

    if user_text.lower() == "exit":
        print("Program stopped.")
        break

    if user_text.strip() == "":
        print("Empty input is not allowed.")
        continue

    text = user_text.lower()

    positive_count = 0
    negative_count = 0

    for word in positive_words:
        if word in text:
            positive_count += 1

    for word in negative_words:
        if word in text:
            negative_count += 1

    print("Positive words found:", positive_count)
    print("Negative words found:", negative_count)

    if positive_count > negative_count:
        print("AI Result: Positive")
    elif negative_count > positive_count:
        print("AI Result: Negative")
    else:
        print("AI Result: Neutral")