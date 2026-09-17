import streamlit  as st 
import joblib 

st.title('Welcome to My Streamlit App!')

class_names = ['Failed', 'Passed']

model = joblib.load('Log_reg.pkl')

age = st.number_input("Enter Your age")
physical_score = st.number_input("Enter Your Physical Score")

data = [[age, physical_score]]
if st.button("Predict",type="primary"):
    prediction = model.predict(data)
    st.success(f"The predicted value is: {class_names[prediction[0]]}")