from analyzer import TextAnalyzer

print("\n-------- TEXT ANALYZER ------\n")

choice = input("1. Enter text\n2. Load file\nChoose: ")

if choice == "1":
    text = input("Enter your text:\n")

else:
    filename = input("Enter filename: ")

    try:
        with open(filename, 'r') as file:
            text = file.read()

    except FileNotFoundError:
        print("File not found!")
        exit()

analyzer = TextAnalyzer(text)

print("\nTOP WORDS:")
print(analyzer.word_frequency())

print("\nSENTIMENT:")
print(analyzer.sentiment_analysis())

print("\nREADING TIME:")
print(analyzer.reading_time(), "minutes")

print("\nSUMMARY:")
print(analyzer.summarize())

print("\nSPELL CHECKED TEXT:")
print(analyzer.spell_check())

with open("report.txt", "w") as report:

    report.write("TEXT ANALYSIS REPORT\n")

    report.write("\nTOP WORDS:\n")
    report.write(str(analyzer.word_frequency()))

    report.write("\n\nSENTIMENT:\n")
    report.write(str(analyzer.sentiment_analysis()))

    #report.write("\n\nSUMMARY:\n")
    #report.write(analyzer.summarize())