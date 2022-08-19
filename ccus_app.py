# Import Python Libraries
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

# from streamlit_option_menu import option_menu

# Desing of the app
st.set_page_config(page_title="CCUS app")
# Create title of web app
st.title("CO2 Emissions App")

# List of options
options = st.sidebar.radio(
    "Choose your option",
    ("Home", "Refineries data", "Thermal plants data", "Surface Facilities"),
)

if options == "Home":
    st.header("""-**Objectives:** App for view the ccus potential: """)
    st.header("""-**Methodology:**""")
    # Load image
    image = Image.open("resources/ccs.jpg")
    st.image(image)
    st.caption("*CCUS Framework*")
    # Load video
    video = open("resources/ccus.mp4", "rb")
    st.video(video)
    st.caption("*CCUS Value Chain*")
