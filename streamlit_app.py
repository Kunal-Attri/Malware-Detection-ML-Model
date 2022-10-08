import os
import streamlit as st

from file_checker import checkFile

st.title("Malware Detection using Random Forest Algorithm")
st.markdown("""### Demo: [Youtube]() 
Malwares can wreak havoc on a computer and its network. Hackers use it to steal passwords, delete files and render computers inoperable. A malware infection can cause many problems that affect daily operation and the long-term security of your company.

This is a python program for detecting whether a given file is 
a probable malware or not! It uses [Random Forest Algorithm](https://en.wikipedia.org/wiki/Random_forest) for 
classification.""")
st.markdown("##### Dataset used: [Kaggle](https://www.kaggle.com/competitions/malware-detection/data)")
st.subheader("Try yourself:-")

file = st.file_uploader("Upload a file to check for malwares:", accept_multiple_files=True)
if len(file):
    with st.spinner("Checking..."):
        for i in file:
            open('malwares/tempFile', 'wb').write(i.getvalue())
            legitimate = checkFile("malwares/tempFile")
            os.remove("malwares/tempFile")
            if legitimate:
                st.write(f"File {i.name} seems *LEGITIMATE*!")
            else:
                st.markdown(f"File {i.name} is probably a **MALWARE**!!!")
