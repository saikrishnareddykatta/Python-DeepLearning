from bs4 import BeautifulSoup
import requests
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk import trigrams
from nltk import ne_chunk

URL = 'https://en.wikipedia.org/wiki/Google'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
list = []
file = open("input.txt", "w", encoding='utf-8')
file.write(soup.body.text.encode('utf-8', "rb").decode('utf-8'))
file.close()

text = open('input.txt', encoding="utf8").read()
print(text)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

# Tokenization
print("Tokenization")
word_tokenization = nltk.word_tokenize(text)
sent_tokenization = nltk.sent_tokenize(text)
print("WORD TOKENIZATION")
print(word_tokenization)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

print("SENTENCE TOKENIZATION")
print(sent_tokenization)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

# POS
print("PARTS OF SPEECH")
POS = nltk.pos_tag(word_tokenization)
print(POS)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

# Stemming
print(" PORTER STEMMING:")
porterStemmer = PorterStemmer()
print(porterStemmer.stem(text))
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

print(" LANCASTER STEMMING:")
lancasterStemmer = LancasterStemmer()
print(lancasterStemmer.stem(text))
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

print(" SNOWBALL STEMMING:")
snowballStemmer = SnowballStemmer('english')
print(snowballStemmer.stem(text))
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

# Lemmatization
print(" LEMMATIZING ")
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(text))
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

#  Trigram
print("TRIGRAMS:")
trig = trigrams(word_tokenization)
for x in trig:
  print(x)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")

# Named Entity Recognition
print("NAMED ENTITY RECOGNITION")
ner = ne_chunk(POS)
print("\nNamed Entity Recognition :", ner)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
