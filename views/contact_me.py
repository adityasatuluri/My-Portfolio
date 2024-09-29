import streamlit as st


try:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@200..900&display=swap');

        h1 {
            font-family: 'Unbounded', sans-serif;
            font-size: 3em;
            color: white;
            margin-bottom: 0.5em;
        }
        </style>

        <h1>CONTACT ME</h1>
        """,
        unsafe_allow_html=True
    )



except Exception:
    st.write("Error")