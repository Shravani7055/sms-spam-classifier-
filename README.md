# SMS Spam Classifier 📱

Spam texts are annoying — so I built a detector. Uses NLP techniques like stemming and TF-IDF vectorization with Naive Bayes to classify SMS messages as spam or not spam.

## Live Demo
🔗 https://lwq78oqkxlqkxgzdqkjwgr.streamlit.app/

## Features
- Detects spam messages in real time
- Trained on 5500+ real SMS messages
- Uses NLP techniques like tokenization, stemming and TF-IDF
- Built with Streamlit for easy interaction

## Tech Stack
- Python
- NLTK
- Scikit-learn
- Streamlit
- Pandas
- Naive Bayes

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Results
- Accuracy: 96%
- Trained on real spam dataset from UCI Machine Learning Repository
