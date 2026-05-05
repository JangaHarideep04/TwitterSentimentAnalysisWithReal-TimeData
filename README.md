# 🐦 Twitter Sentiment Analysis

A Python-based project that analyzes public sentiment on Twitter by classifying tweets into **Positive, Negative, or Neutral** using Natural Language Processing (NLP) techniques.

---

## 📌 Project Overview

This project was developed to understand public opinion on social media by analyzing tweets in real-time. It extracts tweets based on a keyword or hashtag and applies sentiment analysis to identify the overall mood of users.

The project combines **data collection, preprocessing, sentiment analysis, and visualization** to provide meaningful insights.

---

## 🎯 Project Objective

* Analyze real-time tweets
* Classify sentiment (Positive / Negative / Neutral)
* Visualize sentiment distribution
* Understand public opinion trends

---

## 🧠 Methodology (Based on Project Implementation)

The project follows these steps:

### 1️⃣ Data Collection

* Tweets are collected using the **Twitter API (Tweepy)**
* Input: keyword / hashtag and number of tweets

### 2️⃣ Data Preprocessing

* Removal of unwanted characters (URLs, mentions)
* Tokenization
* Stopword removal
* Text cleaning

### 3️⃣ Sentiment Analysis

* **TextBlob** → polarity-based sentiment
* **VADER (NLTK)** → sentiment intensity scores

### 4️⃣ Classification

* Positive → positive score higher
* Negative → negative score higher
* Neutral → scores are equal

### 5️⃣ Visualization

* Pie chart → sentiment percentage
* Bar chart → tweet count

---

## 🚀 Current Implementation (Available Code)

The available implementation includes:

* Command-line based input
* Real-time tweet fetching using Tweepy
* Sentiment analysis using TextBlob and VADER
* Data visualization using Matplotlib
* Output displayed in console and graphs

---

## 🛠️ Technologies Used

* Python
* Tweepy
* TextBlob
* NLTK (VADER)
* Pandas
* Matplotlib
* Termcolor

---

## 📂 Project Structure

```bash id="v8x7m1"
sentiment-analysis/
│
├── sentiment_analysis.py   # Main script (available)
├── README.md              # Documentation
```

---

## ⚙️ How to Run

### 1. Install dependencies

```bash id="r4x8na"
pip install tweepy textblob nltk matplotlib pandas termcolor
```

### 2. Download NLTK data

```python id="f4bn1k"
import nltk
nltk.download('vader_lexicon')
```

### 3. Add Twitter API keys

```python id="8v8w2k"
consumer_key = "YOUR_KEY"
consumer_secret = "YOUR_SECRET"
access_token = "YOUR_TOKEN"
access_token_secret = "YOUR_SECRET"
```

### 4. Run the script

```bash id="7m4rxa"
python sentiment_analysis.py
```

---

## 📊 Output

* Total tweets analyzed
* Number of positive, negative, neutral tweets
* Sentiment percentages
* Pie chart and bar chart visualizations

---

## ⚠️ Note on Implementation

Some parts of the original project (such as extended modules and additional interface components described in the project report) are not included in the current repository due to loss of certain files.

However, the core functionality of:

* Tweet collection
* Sentiment analysis
* Visualization

is fully implemented and working.

---

## 🚧 Limitations

* Cannot detect sarcasm
* Limited contextual understanding
* Works mainly for English tweets
* Depends on Twitter API availability

---

## 🔮 Future Improvements

* Rebuild missing modules from original project
* Add web interface (Flask / Streamlit)
* Use advanced ML models (BERT / LSTM)
* Improve sentiment accuracy
* Add real-time dashboard

---

## 👨‍💻 Author

Harideep Janga
Computer Science Graduate
Interested in Data Science & NLP

---

## 📜 License

This project is for academic and learning purposes.

---

## ⭐ Support

If you found this project useful, give it a ⭐
