
# 📧 Email Spam Detector

This is a machine learning project that detects whether a given message is **Spam** or **Not Spam (Ham)** using a **Naive Bayes classifier** and a **Streamlit web interface**.

---

## 🚀 Features

- ✅ Clean and simple Streamlit UI  
- ✅ Real-time prediction of spam or ham messages  
- ✅ Trained using TF-IDF vectorization and Multinomial Naive Bayes  
- ✅ Lightweight and fast — runs locally in seconds  

---

## 🧠 How it Works

1. The model is trained on the **SMS Spam Collection dataset** from UCI/Kaggle.
2. Text messages are cleaned and processed:
   - Lowercased
   - Stopwords removed
   - Stemming applied
3. A **TF-IDF vectorizer** converts text into numerical features.
4. A **Naive Bayes model** learns the spam/ham patterns.
5. **Streamlit** creates a simple web interface for real-time predictions.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Aasritha-sure/email-spam-detector.git
cd email-spam-detector
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python spam_detector.py
```

This will generate a `spam_model.pkl` file.

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📊 Sample Output

When you enter a message like:

> 🎉 "Congratulations! You've won a \$1000 Amazon gift card!"

The app may predict:

> 🚫 **Spam**

---

## 📦 Dataset

This project uses the **SMS Spam Collection Dataset**, available on [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).

---

## 💡 Future Improvements

* Add more sophisticated models like **SVM** or **BERT**
* Use a larger and more diverse dataset
* Add **accuracy, precision, recall** metrics to the UI
* Deploy the app online using **Streamlit Cloud**

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/00867c97-e290-4e5d-982a-5687c9106750)
![image](https://github.com/user-attachments/assets/9975e0b2-53d8-4f45-b753-964073408dbd)


---

## 🙋‍♀️ Author

Developed by **Sure Aasritha**
🔗 [GitHub Profile](https://github.com/Aasritha-sure)

