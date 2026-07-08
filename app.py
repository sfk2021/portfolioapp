import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.sidebar.title("🚀 Portfolio")

st.sidebar.markdown("""
- 🏠 Home
- 👤 About
- 🛠 Tech Stack
- ⭐ Projects
- ☁️ Azure AI
- ⚡ n8n
- 🖼 Deep Learning
- 🧠 GenAI

- 📬 Contact
""")
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
    background-color: #0F172A;
    color: white;
    
}

.hero {
    padding: 80px 50px;
    border-radius: 32px;

    background:
    linear-gradient(
        135deg,
        #2563EB 0%,
        #06B6D4 50%,
        #8B5CF6 100%
    );

    text-align:center;
    color:white;

    box-shadow:
    0 0 30px rgba(37,99,235,.4),
    0 0 60px rgba(139,92,246,.2);

    margin-bottom:40px;
}
.tech-card {

    background: rgba(17,24,39,.8);

    border: 1px solid rgba(255,255,255,.08);

    border-radius: 20px;

    padding: 20px;

    text-align: center;

    color: white;

    transition: all .3s ease;

    margin-bottom: 15px;

    backdrop-filter: blur(10px);
}

.tech-card:hover {

    transform: translateY(-8px);

    border-color: #2563EB;

    box-shadow:
    0 10px 25px rgba(37,99,235,.35);
}

.tech-icon {

    font-size: 32px;

    margin-bottom: 10px;
}

.tech-title {

    font-weight: 700;

    font-size: 18px;
}
.project-card {

    background: rgba(17,24,39,.75);

    backdrop-filter: blur(12px);

    border:1px solid rgba(255,255,255,.08);

    border-radius:24px;

    padding:25px;

    color:white;

    transition:all .3s ease;
}

.project-card:hover {

    transform:translateY(-8px);

    box-shadow:
    0 10px 30px rgba(37,99,235,.35);
}

.skill-badge {

    display:inline-block;

    padding:10px 18px;

    margin:6px;

    border-radius:999px;

    background:rgba(37,99,235,.15);

    border:1px solid #2563EB;

    color:#60A5FA;

    font-weight:600;

    transition:all .3s ease;
}

.skill-badge:hover {

    background:#2563EB;

    color:white;

    transform:scale(1.05);
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

st.header("📈 Skills Dashboard")

df = pd.DataFrame({
    "Skill":[
        "Python",
        "Machine Learning",
        "Azure AI",
        "Generative AI",
        "n8n",
        "Streamlit"
    ],
    "Level":[95,90,85,85,80,90]
})

fig = px.bar(
    df,
    x="Skill",
    y="Level",
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------------
# LINKS
# -----------------------------------

col1,col2,col3 = st.columns(3)

with col1:
    st.link_button("GitHub", "https://github.com/sfk2021")

with col2:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/saba-khan-791061216/")

with col3:
    st.link_button("📧 Email","saba.sk.khan15@gmail.com")

# -----------------------------------
# KPI
# -----------------------------------

st.divider()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Projects", "10+")
c2.metric("Repositories", "8+")
c3.metric("Technologies", "15+")
c4.metric("Models Built", "5+")
st.header("👤 About Me")

st.markdown("""
Azure AI Engineer Associate certified professional focused on:

- Machine Learning
- Generative AI
- Azure AI Services
- n8n Automation
- Data Analytics
""")

# -----------------------------------
# SKILLS
# -----------------------------------

st.header("🛠️ Tech Stack")

tech_stack = [
("🐍","Python"),
("📊","Pandas"),
("🔢","NumPy"),
("🤖","Scikit-Learn"),
("🧠","TensorFlow"),
("🔥","PyTorch"),
("☁️","Azure AI"),
("💬","Azure OpenAI"),
("🔍","Azure AI Search"),
("📄","Document Intelligence"),
("🚀","Streamlit"),
("⚡","FastAPI"),
("🔄","n8n"),
("🐳","Docker"),
("📂","GitHub")
]

for i in range(0, len(tech_stack), 5):

    cols = st.columns(5)

    for col, tech in zip(cols, tech_stack[i:i+5]):

        icon, name = tech

        with col:
            st.markdown(
                f"""
                <div class="tech-card">
                    <div class="tech-icon">{icon}</div>
                    <div class="tech-title">{name}</div>
                </div>
                """,
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

st.markdown("""
<hr>

<center>

### 🚀 Saba Khan

AI Engineer | Azure AI Engineer Associate

</center>
""", unsafe_allow_html=True)