import streamlit as st
import pandas as pd
import joblib

# --- App Configuration ---
st.set_page_config(
    page_title="Solar Cell Performance Predictor",
    page_icon="☀️",
    layout="wide"
)

# --- Load Assets ---
# Load the trained model pipeline
try:
    model = joblib.load('solar_cell_model.joblib')
except FileNotFoundError:
    st.error("Model file 'solar_cell_model.joblib' not found. Please ensure it's in the same directory.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred loading the model: {e}")
    st.stop()

# --- Load NEW dataset to get unique material options ---
try:
    # This is the line we changed
    df = pd.read_excel('Perovskite_Performance_Metrics_Expanded_Physical_1000.xlsx') 
    
    # Assuming the column names are still 'ETL', 'HTL', 'Perovskite Used'
    etl_options = sorted(df['ETL'].dropna().unique())
    htl_options = sorted(df['HTL'].dropna().unique())
    perovskite_options = sorted(df['Perovskite Used'].dropna().unique())
    
except FileNotFoundError:
    st.error("Dataset 'Perovskite_Performance_Metrics_Expanded_Physical_1000.xlsx' not found.")
    st.stop()
except KeyError as e:
    st.error(f"Error: A column name is incorrect in your new Excel file. Could not find: {e}")
    st.stop()
except Exception as e:
    st.error(f"An error occurred loading the dataset: {e}")
    st.stop()


# --- App UI ---
st.title("☀️ Perovskite Solar Cell Performance Predictor")

st.markdown("""
This app predicts the four key performance metrics of a perovskite solar cell
based on the materials used for its main layers.
""")

# Input form for user to select materials
with st.form("prediction_form"):
    st.header("Select Materials")
    
    # Create dropdown menus for each material layer
    etl_choice = st.selectbox("Electron Transport Layer (ETL)", etl_options)
    htl_choice = st.selectbox("Hole Transport Layer (HTL)", htl_options)
    perovskite_choice = st.selectbox("Perovskite Material", perovskite_options)
    
    # Submit button
    submitted = st.form_submit_button("Predict Performance")

# --- Prediction Logic ---
if submitted:
    # Create a DataFrame from the user's selections
    input_data = pd.DataFrame([{
        'etl': etl_choice,
        'htl': htl_choice,
        'perovskite': perovskite_choice
    }])
    
    # Make a prediction using the loaded model
    try:
        prediction = model.predict(input_data)
        
        # Display the prediction
        st.header("Predicted Performance Metrics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Efficiency (PCE_%)", value=f"{prediction[0][3]:.2f}")
        with col2:
            st.metric(label="Open-Circuit Voltage (Voc_V)", value=f"{prediction[0][0]:.2f}")
        with col3:
            st.metric(label="Short-Circuit Current (Jsc_mA/cm²)", value=f"{prediction[0][1]:.2f}")
        with col4:
            st.metric(label="Fill Factor (FF)", value=f"{prediction[0][2]:.2f}")
        
        st.toast("Prediction Complete!", icon="🎉")
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")