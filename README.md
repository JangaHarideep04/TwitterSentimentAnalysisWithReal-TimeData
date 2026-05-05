# TwitterSentimentAnalysisWithReal-TimeData

# 🐦 Twitter Sentiment Analysis with Real-Time Data

A real-time sentiment analysis system that collects live tweets using the Twitter API and classifies them into **Positive, Negative, or Neutral sentiments** using Natural Language Processing (NLP) techniques. The system also provides interactive visualizations to understand public opinion trends.

---

## 📌 Project Description

With the rapid growth of social media, platforms like Twitter generate massive amounts of user opinions. Understanding these opinions is important for businesses, researchers, and individuals.

This project extracts real-time tweets based on keywords or hashtags and analyzes their sentiment using NLP techniques. It then visualizes the results using graphs and dashboards to make insights easy to understand.

---

## 🎯 Objectives

* Collect real-time tweets using Twitter API
* Perform sentiment analysis (Positive / Negative / Neutral)
* Visualize data using graphs and charts
* Provide insights into public opinion and trends

---

## 🚀 Key Features

* 🔍 Real-time tweet extraction using Twitter API
* 🧠 Sentiment classification using NLP
* 🧹 Data preprocessing (cleaning, tokenization, stopword removal)
* 📊 Data visualization:

  * Bar charts
  * Pie charts
  * Word cloud
  * Sentiment graphs
* 📈 Engagement analysis (likes & retweets)
* 🌐 Web interface using Flask

---

## 🏗️ System Workflow

The system works in three main phases:

### 1️⃣ Data Collection

* Tweets are collected using Twitter API via Tweepy
* Input: keyword / hashtag / number of tweets

### 2️⃣ Data Preprocessing

* Tokenization
* Stopword removal
* Stemming
* Removing URLs, mentions, special characters

### 3️⃣ Sentiment Analysis

* TextBlob is used to calculate sentiment polarity
* Classification:

  * Positive → polarity > 0
  * Neutral → polarity = 0
  * Negative → polarity < 0

---

## 🧠 Methodology

* Tweets are fetched in real-time using API
* Cleaned and processed using NLP techniques
* Sentiment is calculated using TextBlob
* Results are stored and visualized using graphs

The system also uses:

* Bag of Words (BoW)
* Naive Bayes concept (basic classification logic)
* Data visualization for insights

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Tools

* NLTK
* TextBlob
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

### Frameworks

* Flask (Web Application)
* Streamlit (optional UI)

### APIs

* Twitter Developer API
* Tweepy

---

## 📊 Output & Visualizations

The project generates multiple insights:

* 📉 Sentiment distribution (Positive / Negative / Neutral)
* 📊 Bar charts and pie charts
* ☁️ Word cloud for frequent words
* 📈 Time-series analysis (likes & retweets)
* 📊 Polarity vs Subjectivity graph

Users can:

* Enter keywords
* View tweets
* Analyze sentiment in real-time

---

## 📂 Project Structure

```
twitter-sentiment-analysis/
│
├── app.py                 # Main Flask application
├── twitter_client.py      # Twitter API handling
├── tweet_analyzer.py      # Sentiment analysis logic
├── templates/             # HTML frontend
├── static/                # CSS / assets
├── data/                  # Collected data
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Twitter API

Add your API keys in the code:

```python
consumer_key = "YOUR_KEY"
consumer_secret = "YOUR_SECRET"
access_token = "YOUR_TOKEN"
access_token_secret = "YOUR_SECRET"
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📈 Use Cases

* 📊 Brand sentiment analysis
* 📣 Public opinion tracking
* 🏢 Business insights
* 📰 Trend detection
* 🎯 Marketing analysis

---

## 🚧 Limitations

* Cannot detect sarcasm accurately
* Limited support for multiple languages
* Depends on Twitter API access

---

## 🔮 Future Enhancements

* Deep learning models (LSTM / BERT)
* Multi-language sentiment analysis
* Sarcasm detection
* Real-time dashboards (Streamlit / React)
* Improved accuracy using advanced ML models

---

## 👨‍💻 Author

**Naga Venkata Sai Harideep Janga**

* Computer Science Graduate
* Interested in Data Science, NLP & Cloud Systems

---

## 📜 License

This project is for academic and research purposes.

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub and feel free to contribute!
