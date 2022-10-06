# Malware-Detection-ML-Model
### Demo: [Youtube]()
### Try at: [Streamlit](https://kunal-attri-malware-detection-ml-model-streamlit-app-l9q9ae.streamlitapp.com/)
- This is a [Python](https://www.python.org/) program to train Malware Detection ML Model and check if a given file is a probable MALWARE or not!
- It uses [Random Forest](https://en.wikipedia.org/wiki/Random_forest) algorithm for training the ML model.
- I have implemented it in 2 ways:
  - CLI app
  - Streamlit app

NOTE: Don't run any files inside malwares folder, as these are actual malwares taken from [GitHub](https://github.com/Pyran1/MalwareCollection).

## Requirements (installable via pip)
- For running CLI app:
  - [joblib](https://pypi.org/project/joblib/) 
  - [pefile](https://pypi.org/project/pefile/) 
- For running Streamlit app:
  - [streamlit](https://pypi.org/project/streamlit/)
  - joblib
  - pefile
- For training your own model:
  - [numpy](https://pypi.org/project/numpy/) 
  - [pandas](https://pypi.org/project/pandas/) 
  - [scikit-learn](https://pypi.org/project/scikit-learn/)
  - joblib 
  - pefile 

## What I used?
1. [Scikit-learn](https://scikit-learn.org/) - Scikit-learn (formerly scikits.learn and also known as sklearn) is a free software machine learning library for the Python programming language.
   - RandomForestClassifier
   - ExtraTreesClassifier
2. [Malware Dataset](https://www.kaggle.com/competitions/malware-detection/data) - The raw data here was obtained from the malware security partner of Meraz'18 - Annual Techno Cultural festival of IIT Bhilai, the said raw data constituted malware and legitimate files.
3. [Streamlit](https://streamlit.io/) - for GUI - Streamlit is an open-source app framework for Machine Learning and Data Science teams.
4. [Flask](https://flask.palletsprojects.com/) - for distributed system - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

## How to run the program?
1. **Download this GitHub repository**
	- Either Clone the repository
		```
		git clone https://github.com/Kunal-Attri/Malware-Detection-ML-Model.git
		```
	- Or download and extract the zip archive of the repository.

2. **Download & Install requirements**
	- Ensure that you have Python 3 installed.
	- Open terminal in the Repository folder on your local machine.
	- Run the following command to install requirements.
		```
		pip3 install -r requirements.txt
 		```
3. **Run CLI app**
   - Get a file to check for probable malware, and run:
     ```
     python3 main.py [FILENAME]
     ```
   - *Expected Interface*
   <br><img src="images/cli.png?raw=true"><br><br>
4. **Run Streamlit app**
   - Try on web app [*here*](https://kunal-attri-malware-detection-ml-model-streamlit-app-l9q9ae.streamlitapp.com/).
   - or run locally by:
     ```
     streamlit run streamlit_app.py
     ```
   - *Expected Interface*
   <br><img src="images/streamlit.png?raw=true"><br><br>

## References
- [Random Forest Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [About Random Forest Algorithm](https://www.javatpoint.com/machine-learning-random-forest-algorithm)
- [Extra Trees Classifier](https://www.geeksforgeeks.org/ml-extra-tree-classifier-for-feature-selection/)
- [Streamlit](https://docs.streamlit.io/)