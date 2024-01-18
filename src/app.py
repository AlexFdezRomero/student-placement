import streamlit as st 
import pandas as pd 
import joblib 

df = pd.read_csv("data/Student_Placement.csv")

clf = joblib.load("model/student_placement.pkl")

sk_1 = df["Skill 1"].unique()

sk_2 = df["Skill 2"].unique()

st.title('Student job profile')

st.subheader("Alejandro Fernández Romero")

st.text("Introduce tu nivel en cada ámbito: ")

DSA = st.slider("DSA (Data Structures and Algorithms): ", min_value=0, max_value=100, value=50)
DBMS = st.slider("DBMS (Database Management Systems): ", min_value=0, max_value=100, value=50)
OS = st.slider("OS (Operating Systems): ", min_value=0, max_value=100, value=50)
CN = st.slider("CN (Computer Networks): ", min_value=0, max_value=100, value=50)
Mathematics = st.slider("Mathematics: ", min_value=0, max_value=100, value=50)
Aptitude = st.slider("Aptitude: ", min_value=0, max_value=100, value=50)
Communication = st.slider("Communication: ", min_value=0, max_value=100, value=50)
Problem_Solving = st.slider("Problem Solving: ", min_value=0, max_value=100, value=50)
Creativity = st.slider("Creativity: ", min_value=0, max_value=100, value=50)
Hackathons = st.slider("Hackathons: ", min_value=0, max_value=100, value=50)
# Skill_1 = st.selectbox('Skill 1:',
#    ('Javascript', 'HTML/CSS', 'Photoshop', 'GitHub', 'Figma',
#       'Node.js', 'Angular', 'React', 'Python', 'R', 'Tensorflow',
#       'Deep Learning', 'Pytorch', 'Machine Learning', 'C/C++', 'Java',
#       'MYSQL', 'Oracle', 'Linux', 'Ansible', 'BASH/SHELL',
#       'Cisco Packet tracer', 'Wire Shark'))
Skill_1 = st.selectbox('Skill 1:',sk_1)
#Skill_2 = st.selectbox('Skill 2:',
#    ('Photoshop', 'GitHub', 'Figma', 'HTML/CSS', 'Javascript',
#       'Node.js', 'React', 'Angular', 'Pytorch', 'Tensorflow',
#       'Deep Learning', 'Python', 'R', 'Machine Learning', 'MYSQL',
#       'Oracle', 'Linux', 'Java', 'C/C++', 'Wire Shark',
#       'Cisco Packet tracer', 'BASH/SHELL', 'Ansible'))
Skill_2 = st.selectbox('Skill 2:', sk_2)

if st.button("Submit"):

    valor_1 = sk_1.tolist().index(Skill_1)
    valor_2 = sk_2.tolist().index(Skill_2)

    X = pd.DataFrame([
        [DSA, DBMS, OS, CN, Mathematics, Aptitude, Communication, Problem_Solving, Creativity, Hackathons, valor_1, valor_2]], 
        columns=["DSA", "DBMS", "OS", "CN", "Mathmetics", "Aptitute", "Comm", "Problem Solving", "Creative", "Hackathons", "Skill 1", "Skill 2"
                 ])
    prediction = clf.predict(X)[0]
    st.text(f"La predicción indica: {prediction}")
