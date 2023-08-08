# Import the necessary packages
import streamlit as st
import pandas as pd
from pickle import load
import joblib
import pickle
import numpy as np
import math
import os
from config.definitions import ROOT_DIR
from PIL import Image
import matplotlib.pyplot as plt

# Set up the website (name, layout)
st.set_page_config(page_title="MaGeNiuBi", layout="wide")

# Set up the header
with st.container():
    st.header('Resistance of Concrete-Filled Steel Tubular (CFST) Columns Predicted by Machine Learning Models')


