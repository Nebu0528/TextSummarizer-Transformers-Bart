# import modules
from transformers import pipeline
import subprocess

# Summarize Text Function
# Parameters: Text
# Initializes a summarization pipeline from Hugging Face's transformer library
# Summarizer is called with text parameter
# Maximum of 150 words, min of 30
def text_summarizer(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    #clean_up_tokenization_spaces set to false in v4.45 it will be set to false automatically
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False, clean_up_tokenization_spaces=False)
    return summary[0]['summary_text']

#Save Summary to C File Function
#Parameters summary
#Calls the c program to write the summary into a text file 
def save_text_to_c(summary):

    #by splitting the summary into words (each words are tokens)
    #Every word is an argument for the c file to write into
    command = ['./write_summary', *summary.split()]
    subprocess.run(command)

if __name__ == "__main__":

    print("Please input your text below to be summarized (press Ctrl+D or Enter twice to finish):")
    user_input = []
    while True:
        try:
            line = input()
            if line:
                user_input.append(line)
            else:
                break
            #Cltr+D Error for MacOS users
        except EOFError:
            break

    #joins the user inputs into one string
    text = " ".join(user_input)
    
    if text.strip() == "":
        print("No text was given, the program will exit")
    else:
        #C program will write into a text file
        summary = text_summarizer(text)
        save_text_to_c(summary)
