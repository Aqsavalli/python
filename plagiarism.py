def jaccard_similarity(text1, text2):
    
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    return len(intersection) / len(union) if len(union) != 0 else 0

def detect_plagiarism():
    original_text = input("Enter the original text: ")
    submitted_text = input("Enter the submitted text: ")

    similarity = jaccard_similarity(original_text, submitted_text)

    if similarity > 0.5:
        print(f"Plagiarism detected! Jaccard Similarity: {similarity:.2f}")
    else:
        print(f"No plagiarism detected. Jaccard Similarity: {similarity:.2f}")

detect_plagiarism()
