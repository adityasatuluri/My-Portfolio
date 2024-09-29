import streamlit as st
from theme import blue_dark

# Sample data for the sections
summary_text = """
Aspiring computer science student with a solid background in full-stack development and a keen interest in UI/UX design. I enjoy developing efficient, user-friendly applications and am always willing to learn and contribute to novel projects. I'm looking forward to networking with experts who share my enthusiasm for technology and design.
"""

experience_data = [
    ("Graphic Designer - Freelance (Jan 2022 - Dec 2023)", 
     "Created a range of designs from posters and NFTs to 3D art and animations using Adobe Suite, Blender, and Unreal Engine. Designed and optimized the user interface for web applications."),
    ("AWS Intern - ZintoZek (May 2023 - Jun 2023)", 
     "Proficiently trained in utilizing Amazon Web Services (AWS), managing virtual machines, user accounts, security groups, and setting up Glue Jobs using crawlers.")
]

qualifications_data = [
    ("Secondary Education (CBSE)", 
     "Dr. K. L. P. Public School, Guntur<br>Percentage: 84.6% (2018 - 2019)"),
    ("Diploma in Computer Engineering", 
     "A. A. N. M. & V. V. R. S. R. Polytechnic, Gudlavalleru<br>Percentage: 93% (2019 - 2022)"),
    ("Bachelor of Technology in Computer Science and Engineering", 
     "R. V. R. & J. C. College of Engineering, Chowdavaram<br>Current Grade: 8.83 (2022 - Present)"),
]

# Resume file path
resume_file_path = "assets/resume.pdf"


blue_dark()

st.markdown("<h1>ADITYA SATULURI</h1>", unsafe_allow_html=True)

# Summary section
st.markdown("<h2>Summary</h2>", unsafe_allow_html=True)
st.markdown(f'<div class="section-content"><p>{summary_text}</p></div>', unsafe_allow_html=True)

# Experience section with a table
st.markdown("<h2>Experience</h2>", unsafe_allow_html=True)
experience_html = '<div class="section-content"><table><tr><th>Role</th><th>Description</th></tr>'
for role, description in experience_data:
    experience_html += f'<tr><td>{role}</td><td>{description}</td></tr>'
experience_html += '</table></div>'
st.markdown(experience_html, unsafe_allow_html=True)

# Qualifications section with a table
st.markdown("<h2>Qualifications</h2>", unsafe_allow_html=True)
qualifications_html = '<div class="section-content"><table><tr><th>Qualification</th><th>Details</th></tr>'
for qualification, details in qualifications_data:
    qualifications_html += f'<tr><td>{qualification}</td><td>{details}</td></tr>'
qualifications_html += '</table></div>'
st.markdown(qualifications_html, unsafe_allow_html=True)

# Skills section (add your skills_data as needed)
skills_data = [
    "Python", "Java", "HTML", "CSS", "JavaScript", "SQL", 
    "MERN (MongoDB, Express.js, React, Node.js)", "Tailwind CSS", 
    "Streamlit", "PyTorch", "TensorFlow", "Flask", "Git", "AWS", 
]
#"Problem Solving", "Adaptability","Teamwork", "Leadership", "Attention to Detail", "Critical Thinking"


# Skills section with buttons
st.markdown("<h2>Skills</h2>", unsafe_allow_html=True)
skills_html = '<div class="section-content">'
for skill in skills_data:
    skills_html += f'<span class="skill-button">{skill}</span>'
skills_html += '</div><br><br><br>'
st.markdown(skills_html, unsafe_allow_html=True)

# Resume download button
with open('assets/resume.pdf', 'rb') as f:
    st.download_button('Download My Resume', f, file_name='Aditya_Resume.pdf', key='download_button', help='Click to download the full resume', use_container_width=True)
