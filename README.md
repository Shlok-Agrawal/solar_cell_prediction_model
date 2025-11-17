# ☀️ Perovskite Solar Cell Performance Predictor

This is a simple web app built with Streamlit that predicts the performance of a perovskite solar cell based on its materials.

## 🚀 How It Works

This app uses a pre-trained Random Forest model (`solar_cell_model.joblib`) to predict the four key performance metrics (PCE, Voc, Jsc, FF) of a solar cell. The user selects the materials for the ETL, HTL, and Perovskite layers in the sidebar, and the app displays the predicted results.

## 📁 Key Files

* **`app.py`** -- The main Streamlit application script.
* **`solar_cell_model.joblib`** -- The pre-trained machine learning model.
* **`Perovskite_Performance_Metrics_Expanded_Physical_1000.xlsx`** -- The dataset used to populate the dropdown menus.
* **`requirements.txt`** -- A list of all necessary Python libraries for deployment.

## ⚙️ Running Locally

1.  Make sure you have a virtual environment set up.
2.  Install the required libraries --
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Streamlit app --
    ```bash
    streamlit run app.py
    ```
