from pymongo import MongoClient
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Menghubungkan ke MongoDB
client = MongoClient('YOUR_MONGODB_CONNECTION_STRING')
db = client['YOUR_DATABASE']
collection = db['YOUR_COLLECTION']

# Mengambil data dari MongoDB ke dalam DataFrame
data = list(collection.find())
df = pd.DataFrame(data)

# Memastikan hanya menggunakan data yang sudah dilabeli untuk pelatihan
df_labeled = df.dropna(subset=['label'])

# Menggunakan data yang bersih pada kolom "Clean_Text"
X_labeled = df_labeled['Clean_Text']
y_labeled = df_labeled['label']

# Mengubah teks menjadi fitur yang dapat digunakan oleh model
vectorizer = CountVectorizer()
X_labeled_vectorized = vectorizer.fit_transform(X_labeled)

# Membagi data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X_labeled_vectorized, y_labeled, test_size=0.2, random_state=42)

# Melatih model Multinomial Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Memprediksi set pengujian dan mengevaluasi model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Akurasi: {accuracy}")
print("Laporan Klasifikasi:")
print(report)


# # Menggunakan model yang dilatih untuk memprediksi label pada data yang belum dilabeli
# df_unlabeled = df[df['label'].isnull()]
# X_unlabeled = df_unlabeled['Clean_Text']
# X_unlabeled_vectorized = vectorizer.transform(X_unlabeled)
# y_unlabeled_pred = model.predict(X_unlabeled_vectorized)

# # Menyimpan hasil prediksi pada DataFrame dan MongoDB
# for i, label in zip(df_unlabeled.index, y_unlabeled_pred):
#     df.at[i, 'label'] = label
#     collection.update_one({'_id': df.at[i, '_id']}, {'$set': {'label': label}})

# print("Prediksi label untuk data yang belum dilabeli telah disimpan ke MongoDB.")

# # Menggabungkan semua data yang sudah dilabeli dan yang baru dilabeli
# df_all_labeled = df.dropna(subset=['label'])

# # Menggunakan seluruh data yang dilabeli untuk evaluasi model
# X_all_labeled = df_all_labeled['Clean_Text']
# y_all_labeled = df_all_labeled['label']
# X_all_labeled_vectorized = vectorizer.transform(X_all_labeled)

# # Membagi data menjadi set pelatihan dan pengujian untuk evaluasi akhir
# X_train_all, X_test_all, y_train_all, y_test_all = train_test_split(X_all_labeled_vectorized, y_all_labeled, test_size=0.2, random_state=42)

# # Melatih ulang model menggunakan seluruh data yang sudah dilabeli
# model.fit(X_train_all, y_train_all)

# # Memprediksi set pengujian dan mengevaluasi model pada seluruh data yang sudah dilabeli
# y_pred_all = model.predict(X_test_all)
# accuracy_all = accuracy_score(y_test_all, y_pred_all)
# report_all = classification_report(y_test_all, y_pred_all)

# print(f"Akurasi pada seluruh data yang dilabeli: {accuracy_all}")
# print("Laporan Klasifikasi pada seluruh data yang dilabeli:")
# print(report_all)
