import pandas as pd
import re
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, precision_score


def clean_resume(txt):
    txt = re.sub(r'http\S+\s*', ' ', txt)
    txt = re.sub(r'RT|cc', ' ', txt)
    txt = re.sub(r'#\S+', '', txt)
    txt = re.sub(r'@\S+', '', txt)
    txt = re.sub(r'[^\x00-\x7f]', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt)
    return txt


df = pd.read_csv("UpdatedResumeDataSet.csv")


df['Resume'] = df['Resume'].apply(clean_resume)


le = LabelEncoder()
df['Category'] = le.fit_transform(df['Category'])


tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X = tfidf.fit_transform(df['Resume'])
y = df['Category']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = OneVsRestClassifier(LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted'))

# -------- SAVE FILES -------- #
pickle.dump(model, open("clf.pkl", "wb"))        # keep same name
pickle.dump(tfidf, open("tfidf.pkl", "wb"))
pickle.dump(le, open("label_encoder.pkl", "wb"))

print("Model, TF-IDF, and LabelEncoder saved!")
