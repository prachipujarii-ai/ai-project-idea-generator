import streamlit as st
import random
import sqlite3


conn = sqlite3.connect("ideas.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS ideas (
    title TEXT,
    description TEXT,
    tech TEXT,
    level TEXT,
    score INTEGER
)
""")


st.set_page_config(layout="centered")


st.markdown("""
<h1 style="
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(to right, #38bdf8, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
">
    Smart Project Idea Generator
</h1>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.sidebar.header("About Project")
st.sidebar.write("This app generates personalized project ideas based on user skills, interest, and level.")

st.sidebar.subheader("Technologies Used")
st.sidebar.write("- Python")
st.sidebar.write("- Streamlit")
st.sidebar.write("- HTML + CSS")
st.sidebar.write("- JavaScript")

st.sidebar.subheader("Features")
st.sidebar.write("""
- Personalized project ideas  
- Smart scoring system  
- Modern glass UI  
- Save ideas feature  
""")

st.sidebar.subheader("How to Use")
st.sidebar.write("""
1. Enter your skills  
2. Select interest & level  
3. Click Generate Ideas  
4. View and save results  
""")

st.sidebar.subheader("How it Works")
st.sidebar.write("""
- Matches skills with tech stack  
- Filters based on interest  
- Assigns score using rule-based logic  
""")

st.sidebar.subheader("Future Scope")
st.sidebar.write("""
- AI-based recommendations  
- User login system  
- Cloud deployment  
- More project categories  
""")

st.sidebar.subheader("Developer")
st.sidebar.write("""
- Name: Prachi Pujari 
- Course: Engineering (3rd year) 
- Field: AI / Data Science  
""")


st.write("Enter your details to get project ideas!")


skills = st.multiselect(                  #Added
    "Select your skills",
    [
        "Python", "Java", "ML", "SQL",
        "Flutter", "AWS", "Blockchain",
        "HTML", "CSS", "JavaScript"
    ]
)
skills = ",".join(skills)

interest = st.selectbox(                #Added
    "Select your interest",
    [
              "AI",
              "Web Development",
              "Data Science",
              "Cyber Security",
              "Cloud Computing",
              "Mobile App Development",
              "Blockchain",
              "IoT"
    ]
)
level = st.selectbox(
    "Select difficulty level",
    ["Beginner", "Intermediate", "Advanced", "Expert"]    #Added
)

st.markdown("<br>", unsafe_allow_html=True)


def generate_ideas(skills, interest, level):
    ideas = []

    if interest == "AI":
        ideas.append({
            "title": "AI Chatbot for Students",
            "description": "A chatbot that answers student queries.",
            "tech": "Python, NLP",
            "level": level
        })

        ideas.append({
            "title": "Emotion Detection System",
            "description": "Detects user emotion from text.",
            "tech": "Python, Machine Learning",
            "level": level
        })


    elif interest == "Web Development":
        ideas.append({
            "title": "Portfolio Website Generator",
            "description": "Creates portfolio websites automatically.",
            "tech": "HTML, CSS, JavaScript",
            "level": level
        })

        ideas.append({
            "title": "Blog Platform with AI Suggestions",
            "description": "Suggests blog topics using AI.",
            "tech": "Python, Flask",
            "level": level
        })

    elif interest == "Data Science":
        ideas.append({
            "title": "Sales Prediction System",
            "description": "Predicts sales using past data.",
            "tech": "Python, Pandas, ML",
            "level": level
        })

        ideas.append({
            "title": "Student Performance Predictor",
            "description": "Predicts student marks.",
            "tech": "Python, ML",
            "level": level
        })

    elif interest == "Cyber Security":       #Added
        ideas.append({
            "title": "Password Strength Checker",
            "description": "Checks password security level.",
            "tech": "Python, Security",
            "level": level
        })

        ideas.append({
            "title": "Network Intrusion Detector",
            "description": "Detect suspicious network activity.",
            "tech": "Python, Networking",
            "level": level
        })


    elif interest == "Cloud Computing":        #Added
        ideas.append({
            "title": "Cloud File Storage System",
            "description": "Store files on cloud securely.",
            "tech": "AWS, Python",
            "level": level
        })


    elif interest == "Mobile App Development":     #Added
        ideas.append({
            "title": "Fitness Tracker App",
            "description": "Track daily workouts.",
            "tech": "Flutter, Firebase",
            "level": level
        })


    elif interest == "Blockchain":                #Added
        ideas.append({
            "title": "Crypto Wallet App",
            "description": "Simple blockchain wallet.",
            "tech": "Solidity, Python",
            "level": level
        })


    elif interest == "IoT":                      #Added
        ideas.append({
            "title": "Smart Home Automation",
            "description": "Control home devices remotely.",
            "tech": "Arduino, Python",
            "level": level
        })


    skills_lower = skills.lower()

    # Python
    if "python" in skills_lower:
        ideas.append({
            "title": "Python Automation Tool",
            "description": "Automates repetitive daily tasks.",
            "tech": "Python",
            "level": level
        })

    # Java
    if "java" in skills_lower:
        ideas.append({
            "title": "Java Desktop Application",
            "description": "Build a GUI-based application using Java.",
            "tech": "Java, Swing/JavaFX",
            "level": level
        })

    # Machine Learning
    if "ml" in skills_lower or "machine learning" in skills_lower:
        ideas.append({
            "title": "ML Model for Prediction",
            "description": "Build a machine learning model for predictions.",
            "tech": "Python, Scikit-learn",
            "level": level
        })

    # Web Development
    if "web" in skills_lower:
        ideas.append({
            "title": "Full Stack Web App",
            "description": "Create a dynamic web application.",
            "tech": "HTML, CSS, JS, Backend",
            "level": level
        })

    # Data Science
    if "data" in skills_lower:
        ideas.append({
            "title": "Data Analysis Dashboard",
            "description": "Analyze and visualize data.",
            "tech": "Python, Pandas, Matplotlib",
            "level": level

        })

    if "sql" in skills_lower:                 #Added
        ideas.append({
            "title": "Database Management System",
            "description": "Manage student records using SQL.",
            "tech": "SQL, Python",
            "level": level
        })

    if "flutter" in skills_lower:         #added
        ideas.append({
            "title": "Cross Platform Mobile App",
            "description": "Build Android and iOS app.",
            "tech": "Flutter, Dart",
            "level": level
        })

    if "aws" in skills_lower:        #added
        ideas.append({
            "title": "Cloud Deployment Project",
            "description": "Deploy app on AWS cloud.",
            "tech": "AWS, EC2",
            "level": level
        })

    if "blockchain" in skills_lower:       #added
        ideas.append({
            "title": "Blockchain Voting System",
            "description": "Secure online voting system.",
            "tech": "Blockchain, Solidity",
            "level": level
        })


    def load_css():
        with open("styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    load_css()


    def load_html():
        with open("ui.html") as f:
            st.markdown(f.read(), unsafe_allow_html=True)

    load_html()


    random.shuffle(ideas)
    skills_list = skills.lower().split(",")


    for idea in ideas:
        score = 50

        if interest.lower() in idea["title"].lower():
            score += 20

        if idea["level"] == level:
            score += 15

        for skill in skills_list:
            if skill.strip() in idea["tech"].lower():
                score += 10

        score += random.randint(0, 10)

        idea["score"] = score

    return ideas


if "ideas" not in st.session_state:
        st.session_state.ideas = []

if st.button("Generate Ideas"):
    if skills == "":
        st.warning("Please enter your skills")
    else:
        st.session_state.ideas = generate_ideas(skills, interest, level)


if st.session_state.ideas:
    st.subheader("Suggested Project Ideas:")

    for idea in st.session_state.ideas:
        st.markdown(f"""
        <div class="card">
            <div class="title">{idea['title']}</div>
            <p class="desc">{idea['description']}</p>
            <p class="tech">Tech: {idea['tech']}</p>
            <p class="level">Level: {idea['level']}</p>
            <p class="score">Score: {idea['score']}%</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            "<script src='script.js'></script>",
            unsafe_allow_html=True
        )


        score = idea["score"]

        if score > 85:
            label = "Excellent Match"
        elif score > 70:
            label = "Good Match"
        else:
            label = "Average Match"

        st.markdown(f"**{label} ({score}%)**")
        st.progress(score / 100)


if st.button("Save Ideas"):
    for idea in st.session_state.ideas:
        c.execute("INSERT INTO ideas VALUES (?, ?, ?, ?, ?)", (
            idea["title"],
            idea["description"],
            idea["tech"],
            idea["level"],
            idea["score"]
        ))
    conn.commit()
    st.success("Ideas saved successfully!")


if "ideas" in st.session_state:
    data = str(st.session_state["ideas"])

    st.download_button(
        label="Download Ideas",
        data=data,
        file_name="project_ideas.txt",
        mime="text/plain"
    )