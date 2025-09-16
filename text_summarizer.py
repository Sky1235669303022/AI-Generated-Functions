
def summarize_text(text, num_sentences=3):
    """
    Summarizes the given text by extracting the most important sentences.

    Args:
        text (str): The input text to summarize.
        num_sentences (int): The desired number of sentences in the summary.

    Returns:
        str: The summarized text.
    """
    if not text:
        return ""

    # This is a very basic summarization approach.
    # For more advanced summarization, you would typically use libraries
    # like NLTK, spaCy, or more sophisticated machine learning models.

    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]

    # A simple approach: take the first 'num_sentences' sentences.
    # In a real-world scenario, you'd want to rank sentences by importance
    # (e.g., based on word frequency, TF-IDF, or more advanced NLP techniques).
    summary_sentences = sentences[:num_sentences]
    
    return '. '.join(summary_sentences) + ('.' if summary_sentences else '')

# Example Usage:
if __name__ == "__main__":
    long_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    in contrast to the natural intelligence displayed by humans and animals. 
    Leading AI textbooks define the field as the study of "intelligent agents": 
    any device that perceives its environment and takes actions that maximize 
    its chance of successfully achieving its goals. Colloquially, the term 
    "artificial intelligence" is often used to describe machines that mimic 
    "cognitive" functions that humans associate with the human mind, such as 
    "learning" and "problem-solving".

    AI applications include advanced web search engines (e.g., Google Search), 
    recommendation systems (used by YouTube, Amazon, and Netflix), 
    understanding human speech (such as Siri and Alexa), self-driving cars 
    (e.g., Waymo), generative AI (like ChatGPT), and competing at the highest 
    level in strategic game systems (such as chess and Go).
    """

    summary = summarize_text(long_text, num_sentences=2)
    print("Original Text:\n", long_text)
    print("\nSummarized Text (2 sentences):\n", summary)

    summary_long = summarize_text(long_text, num_sentences=4)
    print("\nSummarized Text (4 sentences):\n", summary_long)

    short_text = "This is a short sentence. It has two parts."
    summary_short = summarize_text(short_text, num_sentences=1)
    print("\nShort Text Summary:\n", summary_short)

    empty_text = ""
    summary_empty = summarize_text(empty_text)
    print("\nEmpty Text Summary:\n", summary_empty)
Added a Python function for text summarization.
