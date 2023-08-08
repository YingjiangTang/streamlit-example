# Import the necessary packages
import streamlit as st
import pandas as pd
import numpy as np
import math


# Set up the website (name, layout)
st.set_page_config(page_title="MaGeNiuBi", layout="wide")

# Set up the header
st.header("Resistance of Concrete-Filled Steel Tubular (CFST) Columns Predicted by Machine Learning Models")

# Set up the multi-page choice on the left part
with st.sidebar:
    st.markdown("## **User Input Parameters**")
    columntype = st.selectbox("Column Type", ('Circular Column', 'Circular Beam-Column', 'Rectangular Column', 'Rectangular Beam-Column'))
    st.write("You selected: ", columntype)
    st.write("---")
    st.write("f'c(MPa)")
    df1 = pd.DataFrame({[0]})
    edf1 = st.data_editor(df1)
    st.write("---")
    st.write("fy(MPa)")
    




with st.container():
    st.subheader('Input Parameters')
    st.write("---")
    st.subheader('Nominal (Nn) and Design (Nd) Resistances')

# Resistance factors
phi_CC_GBR=0.85
phi_CBC_XB=0.75
phi_RC_CB=0.85
phi_RBC_CB=0.80


