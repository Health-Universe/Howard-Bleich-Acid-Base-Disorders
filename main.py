import streamlit as st

# Define function to calculate the evaluation of acid base disorders
def calculate_disorder(pH, pCO2, HCO3, Albumin, Na, K, Cl):
    anion_gap = (Na + K) - (Cl + HCO3)
    ag_corrected = anion_gap + 2.5 * (4.5 - Albumin)

    if pH < 7.35:
        if pCO2 > 45:
            return "Respiratory acidosis"
        elif pCO2 < 35:
            return "Metabolic acidosis"
    elif pH > 7.45:
        if pCO2 > 45:
            return "Metabolic alkalosis"
        elif pCO2 < 35:
            return "Respiratory alkalosis"
    
    return "Normal"

# Title of the app
st.title("Howard Bleich's Evaluation of Acid Base Disorders App")

# User inputs
st.markdown("## Input Parameters")
st.markdown("Please enter the following laboratory measurements:")

pH = st.number_input('pH (Normal range: 7.35-7.45)', min_value=0.0, max_value=14.0)
pCO2 = st.number_input('pCO2 in mmHg (Normal range: 35-45 mmHg)', min_value=0.0)
HCO3 = st.number_input('HCO3 in mEq/L (Normal range: 22-28 mEq/L)', min_value=0.0)
Albumin = st.number_input('Albumin in g/dL (Normal range: 3.4-5.4 g/dL)', min_value=0.0)
Na = st.number_input('Na in mEq/L (Normal range: 135-145 mEq/L)', min_value=0.0)
K = st.number_input('K in mEq/L (Normal range: 3.5-5.1 mEq/L)', min_value=0.0)
Cl = st.number_input('Cl in mEq/L (Normal range: 96-106 mEq/L)', min_value=0.0)

if st.button('Calculate'):
    result = calculate_disorder(pH, pCO2, HCO3, Albumin, Na, K, Cl)
    st.markdown("## Results")
    st.markdown("The result represents the probable acid-base imbalance based on the given parameters.")
    st.write(f'The result is: **{result}**')
