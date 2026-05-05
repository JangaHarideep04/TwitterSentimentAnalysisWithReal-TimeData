# 🐦 Twitter Sentiment Analysis

A Python-based project that analyzes public sentiment on Twitter by classifying tweets into **Positive, Negative, or Neutral** using Natural Language Processing (NLP) techniques.

---

## 📌 Project Overview

This project aims to understand public opinion on social media by analyzing tweets in real time. It extracts tweets based on a user-defined keyword or hashtag and applies sentiment analysis to identify the overall mood of users.

The system combines **data collection, preprocessing, sentiment analysis, and visualization** to generate meaningful insights from textual data.

---

## 🎯 Project Objectives

* Analyze real-time tweets
* Classify sentiment (Positive / Negative / Neutral)
* Visualize sentiment distribution
* Understand public opinion trends

---

## 🧠 Methodology

The project follows these steps:

### 1️⃣ Data Collection

* Tweets are collected using the **Twitter API (Tweepy)**
* Input: keyword / hashtag and number of tweets

### 2️⃣ Data Preprocessing

* Removal of unwanted content (URLs, mentions, special characters)
* Tokenization
* Stopword removal
* Text cleaning

### 3️⃣ Sentiment Analysis

* **TextBlob** → polarity-based sentiment
* **VADER (NLTK)** → sentiment intensity scoring

### 4️⃣ Classification

* Positive → positive score is higher
* Negative → negative score is higher
* Neutral → scores are equal

### 5️⃣ Visualization

* Pie chart → sentiment percentage
* Bar chart → tweet count distribution

---

## 🚀 Current Implementation

The current implementation includes:

* Command-line based input
* Real-time tweet fetching using Tweepy
* Sentiment analysis using TextBlob and VADER
* Data visualization using Matplotlib
* Results displayed in console and graphs

---

## 🛠️ Technologies Used

* **Python**
* **Tweepy** (Twitter API)
* **TextBlob**
* **NLTK (VADER)**
* **Pandas**
* **Matplotlib**
* **Termcolor**

---

## 📂 Project Structure

```bash
sentiment-analysis/
│
├── sentiment_analysis.py   # Main script
├── README.md              # Documentation
```

---

## ⚙️ How to Run

### 1. Install dependencies

```bash
pip install tweepy textblob nltk matplotlib pandas termcolor
```

### 2. Download required NLTK data

```python
import nltk
nltk.download('vader_lexicon')
```

### 3. Add Twitter API keys

```python
consumer_key = "YOUR_KEY"
consumer_secret = "YOUR_SECRET"
access_token = "YOUR_TOKEN"
access_token_secret = "YOUR_SECRET"
```

### 4. Run the script

```bash
python sentiment_analysis.py
```

---

## 📊 Output

The program provides:

* Total number of tweets analyzed
* Count of positive, negative, and neutral tweets
* Sentiment percentages
* Pie chart and bar chart visualizations

---

## ⚠️ Important Note

Some components described in the original project report (such as extended modules or interface improvements) are not included in this repository due to missing files.

However, the core functionalities are fully implemented:

* Tweet collection
* Sentiment analysis
* Visualization

---

## 🚧 Limitations

* Cannot detect sarcasm effectively
* Limited contextual understanding
* Works primarily for English tweets
* Depends on Twitter API availability

---

## 🔮 Future Improvements

* Rebuild missing modules from the original project
* Add web interface (Flask / Streamlit)
* Integrate advanced models (BERT / LSTM)
* Improve sentiment accuracy
* Add real-time dashboard

---

## 👨‍💻 Author

**Harideep Janga**
Computer Science Graduate
Interested in Data Science & NLP

---

## 📜 License

This project is for academic and learning purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
