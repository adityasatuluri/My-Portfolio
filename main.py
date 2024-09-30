import streamlit as st
from PIL import Image
from theme import blue_dark


im = Image.open("assets/logo-blue.png")
st.set_page_config(page_title="Aditya Satuluri", page_icon=im, layout="wide")

blue_dark()

#navigation
home = st.Page(
    page="views/home.py",
    title="Home",
    icon="🏠"
)

clustergen = st.Page(
    page="views/cluster_gen.py",
    title="Cluster Gen",
    icon="🧠"
)

flexchat = st.Page(
    page="views/flex_chat.py",
    title="Flex Chat",
    icon="🗨️"
)

psycheck = st.Page(
    page="views/psycheck.py",
    title="PsyCheck",
    icon="❤️‍🩹"
)

contact = st.Page(
    page="views/contact_me.py",
    title="Contact Me",
    icon="📱"
)

chatbot = st.Page(
    page="views/chatbot.py",
    title="Know more about me",
    icon="🤖"
)

pg = st.navigation(
    {
        "Info":[home],
        "Projects":[clustergen, flexchat, psycheck],
        "Contact":[contact]
    }
)
pg.run()


st.logo("assets/menu.png")
st.sidebar.text("Made by Aditya Satuluri😎")