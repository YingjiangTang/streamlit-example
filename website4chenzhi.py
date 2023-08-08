# Import the necessary packages
import streamlit as st
# Data related packages
import pandas as pd
import numpy as np
import math
# File related packages
from io import StringIO
import os



# Set up the website (name, layout)
st.set_page_config(page_title="MaGeNiuBi", layout="wide")

# Set up the header
st.header("Resistance of Concrete-Filled Steel Tubular (CFST) Columns Predicted by Machine Learning Models")

# Set up the multi-page choice on the left part
with st.sidebar:
    st.markdown("## **User Input Parameters**")
    
    # Set up the input for Column Type selected by users
    st.write("Column Type")
    columntype = st.selectbox("Column Type", ('Circular Column', 'Circular Beam-Column', 'Rectangular Column', 'Rectangular Beam-Column'), label_visibility="collapsed")
    st.write("You selected: ", columntype)
    st.write("---")
    
    # Set up the inputs for Material Properties
    st.write("Material Properties")
    col1, col2 = st.columns(2)
    with col1:
        fc = st.number_input("f'c (MPa)")

    with col2:
        fy = st.number_input("fy (MPa)")
    
    st.write("---")

    # Set up the inputs for Cross Section Dimensions
    st.write("Cross Section Dimension")
    
    # Set up the part for user input file
    st.write("Input an Excel file")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        fileExtension = uploaded_file.type
        st.write(fileExtension)
        



    # Get the file name




    




with st.container():
    st.subheader('Input Parameters')
    st.write("---")
    st.subheader('Nominal (Nn) and Design (Nd) Resistances')

# Resistance factors
phi_CC_GBR=0.85
phi_CBC_XB=0.75
phi_RC_CB=0.85
phi_RBC_CB=0.80


