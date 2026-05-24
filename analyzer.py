from collections import Counter
import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

class TextAnalyzer:

    def __init__(self, text):
        self.text = text

    def clean_text(self):
        cleaned = re.sub(r'[^a-zA-Z\s]', '', self.text)
        return cleaned.lower()

    def word_frequency(self):
        cleaned = self.clean_text()

        words = word_tokenize(cleaned)

        stop_words = set(stopwords.words('english'))

        filtered = [
            word for word in words
            if word not in stop_words
        ]

        return Counter(filtered).most_common(10)

    def sentiment_analysis(self):
        blob = TextBlob(self.text)
        return blob.sentiment

    def reading_time(self):
        words = len(self.text.split())
        minutes = words / 200
        return round(minutes, 2)

    def spell_check(self):
        blob = TextBlob(self.text)
        corrected = blob.correct()
        return corrected
    
def summarize(self, sentences_count=3):
        parser = PlaintextParser.from_string(self.text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count)
        return ' '.join(str(sentence) for sentence in summary)