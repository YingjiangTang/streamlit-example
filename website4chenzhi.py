# Import the necessary packages
import streamlit as st


# Set up the website (name, layout)
st.set_page_config(page_title="MaGeNiuBi", layout="wide")

# Set up the header
st.title("Resistance of Concrete-Filled Steel Tubular (CFST) Columns Predicted by Machine Learning Models")

# Set up the multi-page choice on the left part
with st.sidebar:
    st.markdown("## **\color{blue}{User Input Parameters}**")
    columntype = st.selectbox("Column Type", ('Circular Column', 'Circular Beam-Column', 'Rectangular Column', 'Rectangular Beam-Column'))
    st.write("You selected: ", columntype)




with st.container():
    st.subheader('Input Parameters')
    st.write("---")
    st.subheader('Nominal (Nn) and Design (Nd) Resistances')

# Resistance factors
phi_CC_GBR=0.85
phi_CBC_XB=0.75
phi_RC_CB=0.85
phi_RBC_CB=0.80


