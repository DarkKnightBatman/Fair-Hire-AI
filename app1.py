import streamlit as st
from compare import compare_resumes
from PyPDF2 import PdfReader


st.set_page_config(page_title="FairHire AI", layout="wide")


st.markdown("""
<style>
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f5f7fa;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.1);
}
.winner {
    border: 3px solid #00c853;
}
.title {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


def read_file(file):
    if file.type == "application/pdf":
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text
    else:
        return file.read().decode('utf-8', errors='ignore')


st.markdown("<h1 class='title'>⚖️ FairHire AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='title'>Unbiased Resume Comparison System</h4>", unsafe_allow_html=True)

st.write("Upload two resumes. Selection is based on **experience, education, skills, projects, certifications** only.")

# ---------- FILE UPLOAD ----------
col1, col2 = st.columns(2)

with col1:
    file1 = st.file_uploader("📄 Upload Candidate 1 Resume", type=['txt','pdf'], key="1")

with col2:
    file2 = st.file_uploader("📄 Upload Candidate 2 Resume", type=['txt','pdf'], key="2")


if file1 and file2:

    text1 = read_file(file1)
    text2 = read_file(file2)

    f1, f2, s1, s2 = compare_resumes(text1, text2)

    st.divider()
    st.subheader("📊 Candidate Comparison")

    col1, col2 = st.columns(2)

    # ---------- Candidate 1 ----------
    with col1:
        box_class = "card winner" if s1 > s2 else "card"
        st.markdown(f'<div class="{box_class}">', unsafe_allow_html=True)

        st.markdown("### 👤 Candidate 1")
        st.write(f"Experience: {f1['experience']} years")
        st.progress(min(f1['experience']/10, 1.0))

        st.write(f"Education Score: {f1['education']}")
        st.progress(f1['education']/5)

        st.write(f"Skill Score: {f1['skills']}")
        st.progress(min(f1['skills']/10, 1.0))

        st.write(f"Projects: {f1['projects']}")
        st.progress(min(f1['projects']/5, 1.0))

        st.write(f"Certifications: {f1['certifications']}")
        st.progress(min(f1['certifications']/5, 1.0))

        st.markdown(f"### 🧮 Final Score: **{s1}**")
        st.markdown("</div>", unsafe_allow_html=True)

   
    with col2:
        box_class = "card winner" if s2 > s1 else "card"
        st.markdown(f'<div class="{box_class}">', unsafe_allow_html=True)

        st.markdown("### 👤 Candidate 2")
        st.write(f"Experience: {f2['experience']} years")
        st.progress(min(f2['experience']/10, 1.0))

        st.write(f"Education Score: {f2['education']}")
        st.progress(f2['education']/5)

        st.write(f"Skill Score: {f2['skills']}")
        st.progress(min(f2['skills']/10, 1.0))

        st.write(f"Projects: {f2['projects']}")
        st.progress(min(f2['projects']/5, 1.0))

        st.write(f"Certifications: {f2['certifications']}")
        st.progress(min(f2['certifications']/5, 1.0))

        st.markdown(f"### 🧮 Final Score: **{s2}**")
        st.markdown("</div>", unsafe_allow_html=True)

    
    st.divider()
    st.subheader("🏆 Final Decision")

    if s1 > s2:
        st.success("🎉 Candidate 1 Selected (Better overall profile)")
    elif s2 > s1:
        st.success("🎉 Candidate 2 Selected (Better overall profile)")
    else:
        st.info("⚖️ Both candidates are equally strong")

  
    st.subheader("🧠 Explanation")

    st.info("""
This system ensures fairness by ignoring personal attributes like name, gender, caste, or religion.

The decision is based only on:
- Experience
- Education
- Skills
- Projects
- Certifications

This reduces bias and promotes merit-based hiring.
""")
