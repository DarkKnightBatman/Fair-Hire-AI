import streamlit as st
import pickle
import re
from PyPDF2 import PdfReader


clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))



def clean_resume(txt):
    txt = re.sub(r'http\S+\s*', ' ', txt)
    txt = re.sub(r'RT|cc', ' ', txt)
    txt = re.sub(r'#\S+', '', txt)
    txt = re.sub(r'@\S+', '', txt)
    txt = re.sub(r'[^\x00-\x7f]', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt)
    return txt


def main():
    st.title("📄 FairHire AI - Unbiased Resume Screener")

    uploaded_file = st.file_uploader("Upload Resume", type=['txt','pdf'])

    if uploaded_file is not None:

        if uploaded_file.type == "application/pdf":
            pdf = PdfReader(uploaded_file)
            resume_text = ""
            for page in pdf.pages:
                resume_text += page.extract_text()
        else:
            try:
                resume_text = uploaded_file.read().decode('utf-8')
            except:
                resume_text = uploaded_file.read().decode('latin-1')

 
        st.subheader("📃 Resume Preview")
        st.write(resume_text[:500])


        cleaned_resume = clean_resume(resume_text)

        input_features = tfidf.transform([cleaned_resume])


        pred_id = clf.predict(input_features)[0]
        role = le.inverse_transform([pred_id])[0]


        try:
            probs = clf.predict_proba(input_features)
            confidence = max(probs[0]) * 100
            st.success(f"🎯 Predicted Role: {role} ({confidence:.2f}%)")
        except:
            st.success(f"🎯 Predicted Role: {role}")


        st.subheader("⚖️ Fairness Analysis")

        neutral_text = re.sub(
            r'\b(he|she|him|her|male|female|mr|mrs)\b',
            '',
            cleaned_resume,
            flags=re.I
        )

        neutral_features = tfidf.transform([neutral_text])
        neutral_pred = clf.predict(neutral_features)[0]
        neutral_role = le.inverse_transform([neutral_pred])[0]

        st.write(f"Prediction without gender words: **{neutral_role}**")

        if neutral_pred != pred_id:
            st.error("⚠️ Bias detected: Prediction changed after removing gender words")
        else:
            st.success("✅ No significant bias detected")

  
        st.subheader("🔍 Top Keywords Detected")

        feature_names = tfidf.get_feature_names_out()
        vector = input_features.toarray()[0]

        top_indices = vector.argsort()[-10:][::-1]
        words = [feature_names[i] for i in top_indices if vector[i] > 0]

        st.write(words)

# Run
if __name__ == "__main__":
    main()
