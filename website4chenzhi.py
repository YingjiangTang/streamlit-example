# Import the necessary packages
import streamlit as st
import pandas as pd
import joblib
import pickle
import numpy as np
import math
import os
import matplotlib.pyplot as plt

# Set up the website (name, layout)
st.set_page_config(page_title="MaGeNiuBi", layout="wide")

# Set up the header
with st.container():
    st.header('Resistance of Concrete-Filled Steel Tubular (CFST) Columns Predicted by Machine Learning Models')


# Load models and scalers
# Circular columns
CC_GBR=joblib.load(os.path.join(ROOT_DIR,'CFST_Circ_Columns_GBR.joblib'))
CC_GBR_sc=pickle.load(open(os.path.join(ROOT_DIR,'CFST_Circ_Columns_GBR.pkl'),'rb'))


