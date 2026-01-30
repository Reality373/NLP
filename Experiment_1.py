# Removal of Stop_words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords from NLTK
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

# Sample text
text = input("Enter the text: ")
print("Original Text:", text)

# Tokenize the text
tokens=word_tokenize(text.lower())
stop_words=set(stopwords.words('english'))
filtered_words=[word for word in tokens if word not in stop_words]
print("Token", tokens)
print("After stopwords :", filtered_words)

