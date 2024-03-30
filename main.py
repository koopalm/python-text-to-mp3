import pyttsx3
import PyPDF2

# Function that turns pdf file to text
def pdf_to_text(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text

# Function that stores the text as a mp3 file
def text_to_mp3(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Main program. 
def main():
    pdf_file = 'book.pdf'
    output_file = 'output.mp3'

    text = pdf_to_text(pdf_file)
    text_to_mp3(text, output_file)

    print(f"PDF file '{pdf_file}' has been turned into a MP3 file '{output_file}'.")

if __name__ == "__main__":
    main()
