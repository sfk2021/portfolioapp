import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Saba Khan | AI Engineer Portfolio",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #F8FAFC;
}

.hero {
    padding: 60px;
    border-radius: 30px;
    background: linear-gradient(135deg,#2563EB,#06B6D4);
    color: white;
    text-align: center;
    box-shadow: 0 20px 50px rgba(37,99,235,0.25);
}

.project-card {
    background: white;
    border-radius: 24px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.skill-badge {
    display:inline-block;
    padding:10px 16px;
    margin:5px;
    border-radius:999px;
    background:#EFF6FF;
    color:#2563EB;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HERO
# -----------------------------------

st.markdown("""
<div class="hero">
<h1>🚀 Saba Khan</h1>
<h3>AI Engineer | Azure AI Engineer Associate | Machine Learning Developer</h3>
<p>
Passionate AI Engineer specializing in Machine Learning,
Generative AI, Azure AI Services, n8n Automation and Data Analytics.
</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# LINKS
# -----------------------------------

col1,col2,col3 = st.columns(3)

with col1:
    st.link_button("GitHub", "https://github.com/sfk2021")

with col2:
    st.link_button("LinkedIn", "ADD_LINKEDIN_URL")

with col3:
    st.write("📧 ADD_EMAIL_ADDRESS")

# -----------------------------------
# KPI
# -----------------------------------

st.divider()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Projects", "10+")
c2.metric("Repositories", "8+")
c3.metric("Technologies", "15+")
c4.metric("Models Built", "5+")

# -----------------------------------
# SKILLS
# -----------------------------------

st.header("🛠️ Tech Stack")

skills = [
"Python","Pandas","NumPy","Scikit-Learn",
"TensorFlow","PyTorch","Azure AI",
"Azure OpenAI","Azure AI Search",
"Document Intelligence","Streamlit",
"FastAPI","n8n","Docker","GitHub"
]

for skill in skills:
    st.markdown(
        f"<span class='skill-badge'>{skill}</span>",
        unsafe_allow_html=True
    )

# -----------------------------------
# FEATURED PROJECTS
# -----------------------------------

st.header("⭐ Featured Projects")

projects = [
    (
        "🏠 House Price Predictor",
        "Random Forest Regression",
        "https://github.com/sfk2021/HousePricePredictor",
        "https://housepricepredictor-randomforestregressionmodel.streamlit.app/"
    ),
    (
        "💰 Loan Approval AI",
        "Logistic Regression",
        "https://github.com/sfk2021/LoanApprovalAILogisticRegression",
        "https://loanapprovalailogisticregressionmodel.streamlit.app/"
    ),
    (
        "👥 Customer Segmentation",
        "K-Means Clustering",
        "https://github.com/sfk2021/CustomerSegmentation",
        "https://customersegmentation-k-meanclustering.streamlit.app/"
    ),
    (
        "📉 Customer Churn Predict AI",
        "Classification Model",
        "https://github.com/sfk2021/CustomerChurnPredictAIClassificationML",
        "https://customerchurnpredictaiclassificationmlalgorithm.streamlit.app/"
    ),
    (
        "🧹 CleanData AI",
        "Data Cleaning Dashboard",
        "https://github.com/sfk2021/datacleaningapp",
        "https://datacleaningappprofessional.streamlit.app/"
    )
]

for title, desc, github, demo in projects:

    st.markdown(
        f"""
        <div class="project-card">
        <h3>{title}</h3>
        <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    a,b = st.columns(2)

    with a:
        st.link_button("GitHub Repository", github)

    with b:
        st.link_button("Live Demo", demo)

# -----------------------------------
# AZURE AI
# -----------------------------------

st.header("☁️ Azure AI Projects")

st.link_button(
    "Azure AI Projects Repository",
    "https://github.com/sfk2021/AI-Projects"
)

st.link_button(
    "Azure Transcriber App",
    "https://github.com/sfk2021/transcriber_app"
)

# -----------------------------------
# N8N
# -----------------------------------

st.header("⚡ n8n Automation Projects")

st.link_button(
    "n8n AI Chatbot",
    "https://github.com/sfk2021/n8nChatbot"
)

# -----------------------------------
# GENERATIVE AI
# -----------------------------------

st.header("🧠 Generative AI Projects")

st.markdown("""
- RAG Chatbot
- PDF Question Answering
- Resume Analyzer
- AI Research Assistant
- Multi-Document Chat
""")

# -----------------------------------
# DEEP LEARNING
# -----------------------------------

st.header("🖼️ Deep Learning Projects")

st.markdown("""
- Plant Disease Detection
- Image Classification
- Object Detection
- CNN Models
- Transfer Learning
""")

# -----------------------------------
# CONTACT
# -----------------------------------

st.header("📬 Contact")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

st.button("Send Message")

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.markdown("""
<center>
Built with ❤️ using Python, Streamlit,
Azure AI, Machine Learning and Generative AI
</center>
""", unsafe_allow_html=True)