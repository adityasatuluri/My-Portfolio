import streamlit as st


def blue_dark():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@200..900&display=swap');

        body {
            color: white;
            background-color: #0E1117;
            font-family: 'Unbounded', sans-serif;
            font-weight: 200;
        }

        h1, h2 {
            font-family: 'Unbounded', sans-serif;
            color: #7ed3f4;
        }

        h1 {
            font-size: 3em;
            margin-bottom: 0.5em;
        }

        h2 {
            font-size: 2em;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }



        table {
            width: 100%;
            border-collapse: collapse;
            border-radius: 5px; /* Rounded corners */
            overflow: hidden; /* Ensure borders are rounded */
        }

        th, td {

            text-align: left;
            border: 1px solid #7ed3f4;

        }

        th {
            background-color: #026aa2;
            color: white;
        }

        tr:hover {
            background-color: rgba(126, 211, 244, 0.1); /* Hover effect for rows */
        }

        .skill-button {
            display: inline-block;
            padding: 0.5em 1em;
            margin: 0.2em;
            border-radius: 15px;
            color: white;
            font-size: 0.9em;
            font-weight: 500;
            text-align: center;
            border: 0.5px solid #6B8792;
        }

        
        .skill-button:hover {
            background-color: rgba(126, 211, 244, 0.4); /* Darker on hover */
        }
        

        .stDownloadButton {
            background-color: #0E1117;
            color: #7ed3f4;
        }


        .stSidebar{
            background-color:#060E11;
            
        }

        .q-container{
            background-color: #001923;
            border-radius: 10px;
            #width:80%;
        }
        .r-container{
            background-color: #153846;
            padding: 15px;
            border-radius: 10px;
            #width:80%;
        }

        .stChatMessage{
            background-color: transparent;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
        <style>
            *{
                font-weight:200;
            }
        </style>
        """,
        unsafe_allow_html=True
    )