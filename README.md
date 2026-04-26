# Spam-Classifier
A machine learning-based spam classifier using NLP techniques. It uses TF-IDF for feature extraction and Naive Bayes for classification. Includes model comparison, cross-validation, and threshold tuning to improve performance and reduce false positives.


Spam Classifier using NLP & Machine Learning

📌 Overview

This project is a machine learning-based spam classifier that predicts whether a message is spam or not. It uses natural language processing techniques to convert text into numerical features and applies classification algorithms to detect spam patterns.

Features:-

Text preprocessing using TF-IDF
Multiple model comparison
High accuracy (~98%) with Naive Bayes
Cross-validation for reliable evaluation
Threshold tuning to reduce false positives
Error analysis on real-world edge cases

🧠 Approach:- 

1. Text Processing
Converted text to lowercase
Removed stopwords
Used TF-IDF to extract important words
Included n-grams (1,2) for better context

Instead of heavy manual preprocessing, TF-IDF handled most of the work efficiently.

2. Feature Extraction

Used TF-IDF to convert text into vectors:

Words with high importance get higher weight
Rare but important words are emphasized

3. Models Used
   
Naive Bayes (MultinomialNB) 
And also comaprision of other model It perform well & good results. (Simple Model)

Results

Model	        Accuracy	   Precision
Naive Bayes:	~98.4%	     1.0


👉 Naive Bayes performed best due to its probabilistic nature on text data.

🔍 Cross Validation
Applied 10-fold cross-validation
Average accuracy ~95–96%

👉 Showed that single test accuracy was slightly optimistic.

⚠️ Error Analysis:-

Case 1:
“Call me now, it’s urgent”

Initial Prediction: Spam ❌
Issue: Words like “call” and “urgent” had high spam probability, leading to false positive

✅ Fix Applied:
Implemented decision threshold tuning using predicted probabilities.
Increased threshold to reduce false positives.

Final Outcome:
Correctly classified as Not Spam 

Case 2:

“You won free internship at Google” → predicted spam

Reason:

Words like “free”, “won”, “apply now” dominate prediction
Model does not understand real-world context

⚙️ Improvements

Threshold Tuning
Default threshold = 0.5
Adjusted threshold to reduce false positives

👉 Helped correctly classify borderline messages

🧠 Key Learnings:-

Feature representation matters more than model complexity
Simple models like Naive Bayes can outperform complex ones
Accuracy alone is not enough → precision and recall matter
Models depend heavily on training data quality
No contextual understanding in classical models

🚧 Limitations:-

Cannot understand sentence meaning
Sensitive to keyword dominance
Depends on dataset quality
May fail on modern spam or phishing messages

Future Improvements:-

Use deep learning models (LSTM / Transformers)
Add contextual understanding
Include metadata (links, sender info)
Use larger and more diverse dataset

🛠️ Tech Stack:-
Python
Scikit-learn
NLTK
Pandas / NumPy

🎯 Conclusion

This project demonstrates not only building a spam classifier but also analyzing model performance, understanding limitations, and improving predictions using techniques like threshold tuning and cross-validation.

⭐ Final Note
This project focuses on practical machine learning skills:-

model comparison
error analysis
real-world thinking


*** What I learn from this Project ?

This project helped me develop a deeper understanding of how real-world spam classifiers work, including how errors occur, how models can be fine-tuned, and the importance of contextual word patterns. It also highlights that model evaluation is not limited to accuracy and precision, but must consider real-world behavior and production-level challenges.
