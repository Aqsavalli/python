def sentiment_analysis(text, positive_words, negative_words):
    words = text.lower().split()

    positive_count = 0
    negative_count = 0

    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        return 'Positive'
    elif negative_count > positive_count:
        return 'Negative'
    else:
        return 'Neutral'

positive_input = ['good', 'super','satisfied', 'great']
negative_input = ['notgood', 'notsatisfied', 'bad']

text_input = input("Enter a sentence for sentiment analysis: ")

result = sentiment_analysis(text_input, positive_input, negative_input)

print(f"Sentiment: {result}")
