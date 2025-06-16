import PyPDF2
import re
from collections import Counter
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')git 

# === Settings ===
PDF_PATH = 'MAIN.pdf'   # <-- metti qui il nome del tuo file PDF
MIN_WORD_LENGTH = 4
TOP_N = 20

# === Stopwords inglesi ===
stop_words = set(stopwords.words('english'))

# === Estrai testo dal PDF ===
with open(PDF_PATH, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

# === Pulizia e conteggio parole ===
words = re.findall(r'\b[a-zA-Z]{%d,}\b' % MIN_WORD_LENGTH, text.lower())
filtered_words = [w for w in words if w not in stop_words]
counts = Counter(filtered_words)
most_common = counts.most_common(TOP_N)

# === Output ===
print(f"\nTop {TOP_N} words (min {MIN_WORD_LENGTH} letters, no common words):\n")
for word, freq in most_common:
    print(f"{freq:4d}  {word}")
