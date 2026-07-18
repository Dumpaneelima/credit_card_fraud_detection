import streamlit as st
import joblib
import numpy as np

#load the model
model=joblib.load("best_model.pkl")
# load the scaler
scaler=joblib.load("scaler.pkl")

st.title("Credit Card Fraud Detection")
st.write("Enter the transaction features to predict if it's's genuine or fraud")
 
#### predict button
feature_names=['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
features=[]
for i in range(30):
    value=st.number_input(f"Feature{i+1}",value=0.0)
    features.append(value)


input_data=np.array([features])


    # scale the input data
scaler_input=scaler.transform(input_data)

    ##make prediction
if st.button("Predict"):
   prediction=model.predict(scaler_input)
   if prediction[0]==0:
      st.success("✅normal transaction")
   else:
      st.error("🚨fraud transaction")

                         