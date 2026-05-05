# 🐦 Twitter Sentiment Analysis with Real-Time Data

A comprehensive Python-based project that performs sentiment analysis on Twitter data by classifying tweets into **Positive, Negative, or Neutral** categories using Natural Language Processing (NLP) techniques.

This project demonstrates how real-time social media data can be processed, analyzed, and visualized to understand public opinion trends.

---

## 📌 Project Overview

With the rapid growth of social media platforms like Twitter, large volumes of user-generated data are produced every second. Analyzing this data can provide valuable insights into public perception, customer feedback, and market trends.

This project focuses on extracting tweets using a keyword or hashtag and analyzing their sentiment using NLP techniques. The results are then visualized using charts to provide a clear understanding of sentiment distribution.

The project integrates multiple components:

* Data collection using Twitter API
* Data preprocessing and cleaning
* Sentiment analysis using NLP models
* Visualization of results

---

## 🎯 Objectives

The main objectives of this project are:

* To collect real-time tweets using Twitter API
* To preprocess textual data for analysis
* To classify tweets into Positive, Negative, or Neutral categories
* To visualize sentiment distribution using graphs
* To understand how public opinion varies based on topics

---

## 🧠 Concept: What is Sentiment Analysis?

Sentiment analysis (also known as opinion mining) is a Natural Language Processing technique used to determine whether a piece of text expresses a **positive, negative, or neutral sentiment**.

It is widely used in:

* Brand monitoring
* Customer feedback analysis
* Market research
* Social media analytics

---

## 🏗️ System Architecture / Workflow

The project follows a structured pipeline:

### 1️⃣ Data Collection

* Tweets are collected using the **Twitter API via Tweepy**
* User provides:

  * Keyword or hashtag
  * Number of tweets

---

### 2️⃣ Data Preprocessing

Before analysis, raw tweets are cleaned:

* Removal of:

  * URLs
  * Mentions (@user)
  * Special characters
* Tokenization of text
* Stopword removal
* Text normalization

---

### 3️⃣ Sentiment Analysis

Two NLP approaches are used:

#### 🔹 TextBlob

* Lexicon-based sentiment analyzer
* Provides:

  * Polarity score (-1 to +1)
* Helps determine overall sentiment

#### 🔹 VADER (NLTK)

* Rule-based sentiment analyzer
* Returns scores:

  * Positive
  * Negative
  * Neutral
  * Compound score

---

### 4️⃣ Sentiment Classification

Each tweet is classified as:

* **Positive** → if positive score is higher
* **Negative** → if negative score is higher
* **Neutral** → if scores are equal

---

### 5️⃣ Visualization

The results are displayed using graphs:

* 📊 Pie Chart → Sentiment percentage
* 📉 Bar Chart → Number of tweets per category

---

## 🚀 Features

### ✔ Currently Implemented

* Command-line interface (CLI)
* Real-time tweet fetching using Tweepy
* Dual sentiment analysis (TextBlob + VADER)
* Sentiment classification (Positive / Negative / Neutral)
* Visualization using Matplotlib
* Percentage-based sentiment distribution

---

### ⚠️ Originally Designed / Extended Features (from project scope)

Based on the original project design :

* Web interface using Flask
* Word cloud generation
* Likes and retweets analysis
* Tweet translation to English
* Enhanced dashboards

Note: Some of these components are not included in the current repository due to missing files.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Tools

* Tweepy → Twitter API integration
* TextBlob → Sentiment polarity
* NLTK (VADER) → Sentiment scoring
* Pandas → Data handling
* Matplotlib → Visualization
* Termcolor → Console output styling

---

## 📂 Project Structure


```bash
twitter-sentiment-analysis/
│
├── sentiment_analysis.py   # Main script (core logic)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

---

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Download required NLTK data

```python
import nltk
nltk.download('vader_lexicon')
```

---

### Step 4: Configure Twitter API Keys

You will be prompted to enter your Twitter API keys securely at runtime. **Do not hardcode your keys in the script.**

⚠️ Important: Never upload your API keys to public repositories.

---

## ▶️ Running the Project

```bash
python sentiment_analysis.py
```

---

## 🧪 Example Input

```
Enter keyword: Space
Enter number of tweets: 100
```

---

## 📊 Output

The program provides:

* Total number of tweets analyzed
* Number of positive, negative, and neutral tweets
* Sentiment percentages
* Pie chart visualization
* Bar chart visualization

---

## 📈 Use Cases

This project can be applied in:

* Brand monitoring
* Customer sentiment analysis
* Product feedback analysis
* Social media trend analysis
* Market research

---

## ⚠️ Limitations

* Cannot detect sarcasm or irony
* Limited contextual understanding
* Works mainly with English tweets
* Depends on Twitter API access

---

## 🔮 Future Enhancements

* Add Flask or Streamlit-based web interface
* Implement word cloud visualization
* Add multilingual support with translation
* Integrate deep learning models (BERT, LSTM)
* Improve sentiment accuracy
* Build real-time dashboards

---

## 🧾 Conclusion

This project demonstrates how Natural Language Processing techniques can be applied to real-time social media data to extract meaningful insights. It provides a foundational approach to sentiment analysis and highlights the importance of data-driven decision-making.

---

## 👨‍💻 Author

**Naga Venkata Sai Harideep Janga**
Computer Science Graduate
Interested in Data Science, NLP, and Cloud Systems

---

## 📜 License

This project is intended for academic and learning purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
