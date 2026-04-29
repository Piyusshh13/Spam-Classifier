import streamlit as st
import pickle

# Load model
with open('Pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Spam Classifier", page_icon="📩")

st.title("📩 Email/SMS Spam Classifier")

# Initialize session state
if "message" not in st.session_state:
    st.session_state.message = ""

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Try Spam Example"):
        st.session_state.message = "Congratulations! You won a free iPhone. Claim now!"

with col2:
    if st.button("Try Normal Example"):
        st.session_state.message = "Hey, call me when you're free."


# Single text area (linked to session state)
message = st.text_area("Write a Message", key="message")

# Predict
if st.button("Predict"):
    
    if message.strip() == "":
        st.warning("Enter a message first")
    else:
        prob = model.predict_proba([message])[0][1]
        
        threshold = 0.7
        prediction = "Spam" if prob >= threshold else "Not Spam"
        
        if prediction == "Spam":
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")

        st.info(f"Confidence: {prob:.2f}")
        st.progress(prob)
        
# Footer
st.markdown("---")
st.caption("Model: TF-IDF + Naive Bayes | Includes threshold tuning")        