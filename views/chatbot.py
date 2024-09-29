import streamlit as st
from groq import Groq
import datetime
from theme import blue_dark
from rag_llama import ragLlama


try:
    blue_dark()
    st.title("Chatbot🤖")
    #st.write("Ask the AI...")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'latest_result' not in st.session_state:
        st.session_state['latest_result'] = None
    if 'user_prompt' not in st.session_state:
        st.session_state['user_prompt'] = ""

    groq_api_key = "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"

    if st.session_state['chat_history']:
        for question, answer, timestamp in st.session_state['chat_history'][::-1]:
            with st.container():
                with st.chat_message("question", avatar="assets/user.png"):
                    st.markdown(question)
                with st.chat_message("human", avatar="assets/aditya.png"):
                    st.markdown(f'<div class="r-container">{answer}</div><br>', unsafe_allow_html=True)


    user_prompt = st.chat_input("Ask away!")
    st.session_state['user_prompt'] = user_prompt


    def parse_llama_groq(api_key, user_input):
        client = Groq(api_key=api_key)
        prompt = user_input
        completion = client.chat.completions.create(
            model="llava-v1.5-7b-4096-preview",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=4096,
            top_p=1,
            stream=False,
            stop=None
        )
        message_content = completion.choices[0].message.content
        return message_content

    if user_prompt:
        #response = str(ragLlama(str(user_prompt)))
        response = parse_llama_groq(groq_api_key, user_prompt)
        st.session_state['latest_result'] = response
        found = False
        for i, (question, _, _) in enumerate(st.session_state['chat_history']):
            if question == user_prompt:
                st.session_state['chat_history'][i] = (user_prompt, response, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                found = True
                break

        if not found:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state['chat_history'].insert(0, (user_prompt, response, timestamp))
        st.rerun()



except Exception as e:
    st.write("Error: ", e)





# context = """
#             ADITYA SATULURI +91 9208281688 ⋄Guntur, AP, IN s.aditya.in@gmail.com ⋄ [LinkedIn](https://linkedin.com/in/aditya-satuluri-a250a31a0/)
#             ⋄ [GitHub](https://github.com/adityasatuluri) ### OBJECTIVE Aspiring Software Engineer seeking opportunities to make meaningful 
#             contributions and advance professionally in a dynamic work environment. ### EDUCATION **Bachelor of Technology in Computer Science
#             and Engineering** R. V. R. & J. C. College of Engineering, Chowdavaram (2022 - Present) *Grade*: 8.83 **Diploma in Computer 
#             Engineering** A. A. N. M. & V. V. R. S. R. Polytechnic, Gudlavalleru (2019 - 2022) *Percentage*: 93% **Secondary Education (CBSE)**
#             Dr. K. L. P. Public School, Guntur (2018 - 2019) *Percentage*: 84.6% ### INTERNSHIPS **Data Science and Machine Learning Intern 
#             (Remote)** YBI Foundation (Jun 2024 – Jul 2024) - Developed machine learning models using Logistic Regression and Support Vector 
#             Machines. **AWS Intern (Remote)** ZintoZek, Hyattsville, MD, USA (May 2023 – Jun 2023) - Proficiently trained in utilizing Amazon 
#             Web Services (AWS) offerings, including managing virtual machines, user accounts, security groups, and setting up Glue Jobs using 
#             crawlers to connect with databases. ### SKILLS **Languages and Scripts**: Python, Java, HTML, CSS, JavaScript, SQL. **Technologies
#             and Frameworks**: MERN, Tailwind CSS, Cloud Computing, Git. **Softwares**: Framer, VS Code, Figma (UI/UX Design), AWS. **Soft 
#             Skills**: Problem-Solving, Adaptability, Teamwork, Leadership, Attention to Detail, Critical Thinking. ### PROJECTS **AI Web 
#             Scraper** (Python) – Sep 2024 [GitHub: Ai Web Scraper](https://github.com/adityasatuluri/Ai-Web-Scraper) - Built an AI-powered 
#             web scraper using Python, Selenium, and BeautifulSoup to extract and process website data. - Integrated LangChain’s Ollama LLM 
#             for AI-driven content parsing and extraction. - Developed a Streamlit UI for real-time user input and dynamic content parsing. 
#             **FlexChat - Chat Application (MERN)** – Jul 2024 [GitHub: FlexChat](https://github.com/adityasatuluri/flex-chat) - Developed a 
#             real-time chat application with file upload capabilities, authentication, and profile management. - Tech stack: MERN (MongoDB, 
#             Express.js, React, Node.js), Socket.io, JWT, Tailwind CSS, Shadecn, Multer. **PsyCheck - Mental Health App (Flutterflow)** – 
#             Dec 2023 [psycheck.flutterflow.app](https://psycheck.flutterflow.app) - Developed a mental health application with 
#             self-assessments, mood tracking, and locating nearby health centers. - Integrated AI for mental health summaries, precautions, 
#             and solutions. - Runner-up in Smart India Hackathon 2023. - Tech stack: Flutterflow, GPT-4, Firebase. ### CERTIFICATIONS - 
#             **React Basics** – Coursera - **Google UX Specialization** – Coursera - **AWS Academy Graduate** – AWS Academy Cloud Foundations,
#             Amazon Web Services. - **PCAP**: Programming Essentials in Python – OpenEDG Python Institute. ### ACHIEVEMENTS - Secured 2nd Prize in 
#             Rapid ML (Jan 2024) contest hosted by V. R. Siddhartha College of Engineering, Vijayawada. - Finalist in Smart India Hackathon (Dec 2023) 
#             for developing a mental health application with my team. ### LEADERSHIP - Oversee CSE branch newsletter design, collaborating with student 
#             editors across branches, ensuring design consistency. - Led my team for Smart India Hackathon 2023, assigned tasks based on expertise, and 
#             reviewed the prototype viability at each sprint. ### EXTRA-CURRICULAR ACTIVITIES - **Graphic Designer (Freelance)**: Created a range of 
#             designs from posters, NFTs to 3D art and animations using Adobe Suite, Blender, and Unreal Engine. - **Innovation Design Entrepreneurship 
#             (IDE) Bootcamp** (Jan 2024): Engaged in a 5-day intensive program emphasizing hands-on learning, exploring diverse product design 
#             methodologies, and applying design thinking principles. - **ACM Student Member (2023 - Present)**: Acted as the designer and student 
#             coordinator for Technizen, an intercollegiate ACM event with over 1600 participants.
# """

# prompt = f"Pretend you are Aditya Satuluri, (i.e, me), answer the based on the {context}"
