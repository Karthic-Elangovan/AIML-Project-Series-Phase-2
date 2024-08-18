
# Disease Prediction System using Machine Learning

## Project Overview
The "Disease Prediction System using Machine Learning" project aims to develop an intelligent system that predicts the likelihood of a person having a particular disease based on various health-related features. The system utilizes machine learning algorithms to analyze historical health data, contributing to early disease detection and proactive healthcare management.

## Project Objectives
1. **Data Collection**:
   - Gathered a diverse dataset containing relevant health features, including age, gender, BMI, blood pressure, cholesterol levels, and family medical history.

2. **Data Preprocessing**:
   - Performed thorough data cleaning and preprocessing to handle missing values and outliers.
   - Normalized or standardized features to ensure a consistent scale.

3. **Feature Selection**:
   - Employed feature selection techniques to identify the most influential variables for disease prediction, enhancing model accuracy.

4. **Model Development**:
   - Implemented various machine learning algorithms such as logistic regression, decision trees, random forests, and support vector machines.
   - Evaluated and compared model performance using metrics like accuracy, precision, recall, and F1-score.

5. **Cross-Validation**:
   - Used cross-validation techniques to assess the generalization performance of the models and mitigate overfitting.

6. **Hyperparameter Tuning**:
   - Fine-tuned the hyperparameters of selected machine learning models to optimize their performance.

7. **Model Interpretability (Optional)**:
   - Enhanced interpretability using SHAP (SHapley Additive exPlanations) values or feature importance plots to provide insights into the factors influencing predictions.

8. **User Interface (Optional)**:
   - Developed a user-friendly interface using Streamlit for users to input their health data and receive predictions.

9. **Integration with Electronic Health Records (EHR) (Optional)**:
   - Explored integration with EHR systems to facilitate seamless information flow between healthcare providers and the prediction system.

10. **Documentation (Optional)**:
    - Provided comprehensive documentation covering data sources, methodology, model architecture, and usage instructions.

11. **Validation and Testing**:
    - Conducted extensive testing to ensure the accuracy, reliability, and robustness of the system.

## File Structure
- **`Disease Prediction using ML.ipynb`**: Jupyter notebook containing the entire workflow of the project, including data preprocessing, model development, and evaluation.
- **`app.py`**: Python script for the web interface using Streamlit, which loads a pre-trained model and predicts the likelihood of heart disease based on user input.

## How to Run the Project
### Prerequisites
- Python 3.10 or higher
- Necessary libraries: `numpy`, `pandas`, `scikit-learn==1.5.1`, `streamlit`, `xgboost`

### Steps to Run
1. **Clone the repository**:
   ```bash
   git clone 'https://github.com/Karthic-Elangovan/AIML-Project-Series-Phase-2'
   cd Disease-Prediction-System
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**:
   - Open and execute the cells in `Disease Prediction using ML.ipynb` to preprocess data, select features, and develop models.

4. **Run the Streamlit Application**:
   - Start the app by running the following command:
     ```bash
     streamlit run app.py
     ```
   - Input your health data in the interface to receive a disease prediction.



## Live Demo
You can access the live demo of the Disease Prediction System here:

[Live Demo](https://heartsense.streamlit.app/)




