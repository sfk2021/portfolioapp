import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Saba Khan | AI Engineer Portfolio",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

.hero {
    padding: 40px;
    border-radius: 20px;
    background: linear-gradient(90deg,#2563EB,#06B6D4);
    text-align:center;
    color:white;
}

.project-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.skill-card {
    background:#EFF6FF;
    padding:15px;
    border-radius:12px;
    text-align:center;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="hero">

<h1>🚀 Saba Khan</h1>

<h3>
AI Engineer | Azure AI Engineer Associate |
Machine Learning Developer
</h3>

<p>
Passionate AI Engineer specializing in Machine Learning,
Generative AI, Azure AI Services, n8n Automation,
and Data Analytics.
</p>

</div>
""", unsafe_allow_html=True)
col1,col2,col3=st.columns(3)

with col1:
    st.link_button(
        "GitHub",
        "https://github.com/sfk2021"
    )

with col2:
    st.link_button(
        "LinkedIn",
        "ADD_LINKEDIN_URL"
    )

with col3:
    st.write("📧 ADD_EMAIL")
    st.divider()

st.header("📊 Portfolio Statistics")

c1,c2,c3,c4=st.columns(4)

c1.metric("Projects",10)
c2.metric("Repositories",8)
c3.metric("Technologies",15)
c4.metric("ML Models",5)
st.divider()

st.header("👨‍💻 About Me")

st.write("""
Azure AI Engineer Associate Certified.

Experienced in:

- Machine Learning
- Generative AI
- Azure AI Services
- n8n Automation
- Data Analytics
- Streamlit Applications
""")
st.divider()

st.header("🛠️ Tech Stack")

skills = [
"Python",
"Pandas",
"NumPy",
"Scikit-Learn",
"TensorFlow",
"PyTorch",
"Azure AI",
"Azure OpenAI",
"Azure AI Search",
"Document Intelligence",
"Streamlit",
"FastAPI",
"n8n",
"Docker",
"GitHub"
]

cols = st.columns(5)

for i,skill in enumerate(skills):
    with cols[i % 5]:
        st.markdown(
            f"<div class='skill-card'>{skill}</div>",
            unsafe_allow_html=True
        )
st.divider()

st.header("🤖 Machine Learning Projects")
with st.container():

    st.subheader("🏠 House Price Predictor")

    st.write(
        "Random Forest Regression model "
        "for predicting house prices."
    )

    c1,c2=st.columns(2)

    with c1:
        st.link_button(
            "GitHub Repository",
            "https://github.com/sfk2021/HousePricePredictor"
        )

    with c2:
        st.link_button(
            "Live Demo",
            "https://housepricepredictor-randomforestregressionmodel.streamlit.app/"
        )
st.subheader("💰 Loan Approval AI")

st.link_button(
    "GitHub",
    "https://github.com/sfk2021/LoanApprovalAILogisticRegression"
)

st.link_button(
    "Live Demo",
    "https://loanapprovalailogisticregressionmodel.streamlit.app/"
)
st.subheader("👥 Customer Segmentation")

st.link_button(
    "GitHub",
    "https://github.com/sfk2021/CustomerSegmentation"
)

st.link_button(
    "Live Demo",
    "https://customersegmentation-k-meanclustering.streamlit.app/"
)
st.subheader("📉 Customer Churn Predict AI")

st.link_button(
    "GitHub",
    "https://github.com/sfk2021/CustomerChurnPredictAIClassificationML"
)

st.link_button(
    "Live Demo",
    "https://customerchurnpredictaiclassificationmlalgorithm.streamlit.app/"
)
st.subheader("🧹 CleanData AI")

st.link_button(
    "GitHub",
    "https://github.com/sfk2021/datacleaningapp"
)

st.link_button(
    "Live Demo",
    "https://datacleaningappprofessional.streamlit.app/"
)
st.divider()

st.header("☁️ Azure AI Projects")

st.subheader("Azure AI Projects")

st.link_button(
    "Repository",
    "https://github.com/sfk2021/AI-Projects"
)

st.subheader("Azure Transcriber App")

st.link_button(
    "Repository",
    "https://github.com/sfk2021/transcriber_app"
)
st.divider()

st.header("⚡ n8n Automation")

st.subheader("n8n AI Chatbot")

st.link_button(
    "Repository",
    "https://github.com/sfk2021/n8nChatbot"
)

st.divider()

st.header("🖼️ Deep Learning Projects")

st.markdown("""
- Plant Disease Detection
- Image Classification
- Object Detection
- Face Mask Detection
- CNN Models
- Transfer Learning
""")
st.divider()

st.header("🧠 Generative AI Projects")

st.markdown("""
- RAG Chatbot
- PDF Question Answering
- AI Research Assistant
- Resume Analyzer
- Multi-Document Chat
- Content Generator
""")
st.divider()

st.header("📬 Contact")

name = st.text_input("Name")

email = st.text_input("Email")

message = st.text_area("Message")

st.button("Send Message")
st.divider()

st.markdown("""
<center>

Built with ❤️ using Python, Streamlit,
Azure AI, Machine Learning and Generative AI

</center>
""", unsafe_allow_html=True)