import streamlit as st
import string
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
        color: white;
    }
    .stTextInput input {
        background-color: #16213e;
        color: white;
        border: 2px solid #e94560;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
    }
    .stButton button {
        background: linear-gradient(90deg, #e94560, #0f3460);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 30px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #0f3460, #e94560);
        transform: scale(1.05);
    }
    h1 {
        text-align: center;
        font-family: 'Courier New', monospace;
        color: #e94560;
        font-size: 3rem;
        text-shadow: 5px 5px 10px #e94560;
    }
    .stCaption {
        font-size: 22px !important;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

ps=PorterStemmer()
def transform_text(massage):
    massage = massage.lower()
    massage = nltk.word_tokenize(massage)
    y = []
    for i in massage:
        if i.isalnum():
            y.append(i)

    massage = y[:]
    y.clear()

    for i in massage:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    massage = y[:]
    y.clear()
    for i in massage:
        y.append(ps.stem(i))
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
st.title("SMS Classifier")
if 'result_shown' not in st.session_state:
    st.session_state.result_shown = False
sms_massage = st.text_input("Enter The SMS")
if st.button("CHECK"):
    if sms_massage:
        transformed_sms = transform_text(sms_massage)
        vecotirzed_sms = tfidf.transform([transformed_sms])
        result = model.predict(vecotirzed_sms)
        st.session_state.result_shown = True
        st.session_state.result = result[0]

if st.session_state.result_shown:
    if st.session_state.result == 1:
        st.markdown("""
            <style>
            .stApp { background-color: #ff4b4b; }
            </style>
            <div style='text-align:center; padding:30px;'>
                <h1 style='color:white; font-size:50px;'>🚨 SPAM DETECTED!</h1>
                <p style='color:white; font-size:20px;'>Be careful! This looks like a spam message!</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .stApp { background-color: #00c853; }
            </style>
            <div style='text-align:center; padding:30px;'>
                <h1 style='color:white; font-size:50px;'>✅ NOT SPAM!</h1>
                <p style='color:white; font-size:20px;'>This message looks safe!</p>
            </div>
        """, unsafe_allow_html=True)

if sms_massage == '':
    st.session_state.result_shown = False