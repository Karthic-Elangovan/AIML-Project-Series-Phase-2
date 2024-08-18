import numpy as np
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open('model.pkl', 'rb'))

def Heart_disease_Prediction(input_data):
    # Convert input data to numpy array and reshape
    input_data_array = np.asarray(input_data, dtype=np.float64)
    input_data_reshaped = input_data_array.reshape(1, -1)
    
    # Predict and return result
    result = loaded_model.predict(input_data_reshaped)
    if result[0] == 1:
        return " 💔💔The person has Heart Disease💔💔 "
    else:
        return " 🩷🩷The person does not have Heart Disease🩷🩷 "

def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Heart Disease Prediction Application</h1>", unsafe_allow_html=True)
    
    # Input fields
    age = st.number_input("Age of person", min_value=0)
    sex = st.number_input("Sex (0: female, 1: male)", min_value=0, max_value=1)
    cp = st.number_input("Chest pain type (0-3)", min_value=0, max_value=3)
    restbps = st.number_input("Resting BP (mm Hg)", min_value=0)
    chol = st.number_input("Serum Cholestoral (mg/dl)", min_value=0)
    fbs = st.number_input("Fasting blood sugar > 120 mg/dl (0 or 1)", min_value=0, max_value=1)
    restecg = st.number_input("Resting electrocardiographic results (0-2)", min_value=0, max_value=2)
    thalach = st.number_input("Maximum heart rate achieved", min_value=0)
    exang = st.number_input("Exercise induced angina (0 or 1)", min_value=0, max_value=1)
    oldpeak = st.number_input("Oldpeak (ST depression induced by exercise relative to rest)", format="%.2f")
    slope = st.number_input("Slope of the peak exercise ST segment (0-2)", min_value=0, max_value=2)
    ca = st.number_input("Number of major vessels (0-3) colored by flourosopy", min_value=0, max_value=3)
    thal = st.number_input("Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect", min_value=0, max_value=2)
    
    # Prediction
    predict = ''
    if st.button('Diagnosis Test Result'):
        predict = Heart_disease_Prediction([age, sex, cp, restbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        st.success(predict)
    
    st.markdown("***")
    
    st.markdown("""
    Sample data to fill: 
    
    25 1 2 130 250 0 1 150 0 1.5 1 1 2 => 💔💔The person has Heart Disease💔💔 """)
    
    st.markdown("""
    About the data to be filled (all data is in numeric form without units) : 
        
    1. age (in numbers)
    2. sex (0 : female, 1 : male)
    3. chest pain type (0-3)
    4. Resting blood pressure (numeric only)
    5. Serum Cholestoral in mg/dl
    6. Fasting blood sugar > 120 mg/dl
    7. Resting electrocardiographic results (values 0,1,2)
    8. Maximum heart rate achieved
    9. Exercise induced angina
    10. Oldpeak = ST depression induced by exercise relative to rest
    11. The slope of the peak exercise ST segment
    12. Number of major vessels (0-3) colored by flourosopy
    13. Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect
    
    Output: Either Heart Disease is present or not (0 or 1)""")
    

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8501))
    st.set_page_config(page_title="Heart Disease Prediction")
    main()
