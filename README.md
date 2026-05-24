# Text Analyzer

A Python-based NLP tool for comprehensive text analysis. This project provides powerful text processing capabilities including sentiment analysis, word frequency analysis, summarization, and more.

## Features

- **Word Frequency Analysis** - Identifies the 10 most common words (excluding stopwords)
- **Sentiment Analysis** - Determines the sentiment polarity and subjectivity of text
- **Reading Time Estimation** - Calculates estimated reading time based on word count
- **Spell Checking** - Automatically corrects spelling errors in text
- **Text Summarization** - Generates concise summaries using LSA-based summarization
- **Report Generation** - Exports analysis results to a text report

## Requirements

- Python 3.x
- textblob
- nltk
- sumy

## Installation

1. Install required packages:
```bash
pip install textblob nltk sumy
```

2. Download required NLTK data:
```bash
python -m textblob.download_corpora
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

## Usage

Run the main program:
```bash
python main.py
```

### Interactive Menu

The program offers two input options:

1. **Enter text directly** - Type or paste text for analysis
2. **Load from file** - Analyze text from an existing file

### Example Output

```
TOP WORDS:
[('python', 15), ('data', 12), ('analysis', 10), ...]

SENTIMENT:
Sentiment(polarity=0.7, subjectivity=0.6)

READING TIME:
2.5 minutes

SUMMARY:
[Summary sentences here...]

SPELL CHECKED TEXT:
Corrected version of input text...
```

## Project Structure

```
text_analyser/
├── analyzer.py       # TextAnalyzer class with analysis methods
├── main.py          # Command-line interface and main execution
├── report.txt       # Generated analysis report
├── sample.txt       # Sample text file for testing
└── README.md        # This file
```

