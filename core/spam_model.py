import string
from django.conf import settings

from joblib import load
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

KNN_MODEL_FILE = settings.BASE_DIR / 'data' / 'spam_model.joblib'
VECTORIZER_FILE = settings.BASE_DIR / 'data' / 'tfidf.joblib'

knn = load(KNN_MODEL_FILE)
tfidf = load(VECTORIZER_FILE)

## from juypter file
def preprocess(text):
    #remove punctuation and lowercase
    text = "".join([t.lower() for t in text if t not in string.punctuation])

    #tokenize
    tokens = text.split(" ") # 'hello world' == 'hello' , 'world'

    #filter out stopwords
    return " ".join(t for t in tokens if t not in ENGLISH_STOP_WORDS)

def predict_spam(text):
    #process each "document"( i.e. each comment)
    processed =[preprocess(text)] 

    #create vectors
    vectors = tfidf.transform(processed)

    #get spam prediction
    return knn.predict(vectors)