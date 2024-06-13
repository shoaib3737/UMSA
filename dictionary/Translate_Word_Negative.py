from googletrans import Translator
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data (if not already downloaded)
nltk.download('punkt')


def translate_to_urdu(words):
    translator = Translator()
    translations = []

    for word in words:
        
        try:
            translation = translator.translate(word, src='en', dest='ur').text
            translations.append(translation)
        except Exception as e:
            # Handle other exceptions
            #print(f"An unexpected error occurred: {e}")
            translations.append(None)
           
        
    return translations

def write_translations_to_file(translations, output_file_path):
    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        for translation in translations:
            ###print(type(translation))
            output_file.write(str(translation) + '\n')

def read_file_in_chunks(input_file_path, chunk_size=10):
    ###print(input_file_path)
    with open(input_file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = [next(file) for _ in range(chunk_size) if next(file, None) is not None]
            if not chunk:
                break
            yield chunk

if __name__ == "__main__":
    input_file_path = 'english_negative_words.txt'  # Replace with your file path
    output_file_path = 'urdu_negative_words.txt'  # Replace with your desired output file path
    
    for i, chunk in enumerate(read_file_in_chunks(input_file_path, chunk_size=10)):
        print(f"Processing Chunk {i + 1} - Records: {len(chunk)}")
        english_words = []
        
        for record in chunk:
            word=record.strip()
            english_words.append(word)
            
        #print(english_words)
        
        urdu_translations = translate_to_urdu(english_words)
        print(urdu_translations,'\n')
        write_translations_to_file(urdu_translations, output_file_path)
            
        # Add any processing logic for each chunk here
