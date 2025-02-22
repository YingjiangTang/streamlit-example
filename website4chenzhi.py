# Import the necessary packages
import streamlit as st
# Data related packages
import pandas as pd
import numpy as np
import math
# File related packages
from io import StringIO
import os

# Define functions used later
def FindIndexfromList(List, Target):
    # This function find a target from a list and return the index of the target's position
    # Inputs:
    # List: a list to carry out the search (input a 1-D vector)
    # Target: the target searched for
    
    # Output:
    # Index of the Target found in this List
    
    # Covert the list into numpy array form
    NPlist = np.asarray(List)
    # Find the total number of elements in this list
    nele = np.shape(NPlist)[0]
    # Initialize the output list
    IndexList = []
    # Loop over the whole list
    for i in range(0, nele):
        if Target in NPlist[i]:
            IndexList.append(i)
              
    # Convert the index list to numpy array form
    IndexList = np.asarray(IndexList)
    return IndexList


# Set up the website (name, layout)
st.set_page_config(page_title="MaGeNiuBi", layout="wide")

# Set up the header
st.header("Resistance of Concrete-Filled Steel Tubular (CFST) Columns Predicted by Machine Learning Models")

Flag = 0

# Set up the first section on the left part
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


# Set up the second section on the left part
with st.sidebar:
    # Set up the part for user input file
    st.markdown("## **User Input File**")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write(uploaded_file)
        st.write(uploaded_file.type)
        fileExtension = uploaded_file.type

        # Add a button for the user to process
        if st.button("Process"):
            if fileExtension == 'text/plain':
                # Read the text file in byte type
                # rawtext = uploaded_file.read()

                # Read the text file and convert as string type
                rawtext = str(uploaded_file.read(), "utf-8")
                
                
            if fileExtension == 'text/csv':
                # Read the table in csv file
                csvdata = pd.read_csv(uploaded_file)
                csvarray = np.asarray(csvdata)
                coldata = csvarray[:,2]
                targdata = "W16"
                finddata = FindIndexfromList(coldata, targdata)
                

            


            
            

    
    



    # Get the file name




    




with st.container():
    st.subheader('Input Parameters')
    st.write("---")
    st.subheader('Nominal (Nn) and Design (Nd) Resistances')
    # st.write(rawtext)
    st.dataframe(csvdata)
    flag = csvarray[0][4]
    st.write(coldata)
    st.write(finddata)



# Resistance factors
phi_CC_GBR=0.85
phi_CBC_XB=0.75
phi_RC_CB=0.85
phi_RBC_CB=0.80


