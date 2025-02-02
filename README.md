# Sentiment Analysis of Tourist Attractions in Bali

## 📌 Overview
Sentiment analysis adalah teknik pengolahan teks yang bertujuan untuk mengidentifikasi dan mengkategorikan opini atau emosi yang terkandung dalam sebuah teks. 

Pada proyek ini, dilakukan analisis sentimen terhadap ulasan tempat wisata di Bali yang diperoleh dari Google Maps. Hasil analisis memberikan wawasan mengenai pengalaman wisatawan serta persepsi mereka terhadap destinasi wisata di Bali.

## 🛠️ Tech Stack
- **Python** (Data Processing & Modeling)
- **Selenium** (Web Scraping)
- **MongoDB** (Database untuk menyimpan ulasan)
- **NLTK & Sastrawi** (Text Preprocessing)
- **Naive Bayes Multinomial** (Sentiment Classification)
- **Matplotlib & Seaborn** (Data Visualization)

## 📊 Workflow
1. **Data Collection**: Menggunakan Selenium untuk mengambil ulasan dari Google Maps.
2. **Data Storage**: Menyimpan data yang dikumpulkan ke dalam MongoDB.
3. **Preprocessing**:
   - Pembersihan teks
   - Normalisasi
   - Tokenisasi
   - Penghapusan stopwords
   - Stemming
4. **Sentiment Analysis**: Menggunakan algoritma **Naive Bayes Multinomial**, yang mencapai akurasi **72%** dalam mengidentifikasi sentimen ulasan.
5. **Visualization**:
   - Heatmap
   - Wordcloud
   - Diagram batang & lingkaran
   - Tren sentimen

## 📈 Key Findings
- Mayoritas ulasan bersentimen **positif**, menunjukkan bahwa pengalaman wisatawan di Bali umumnya **memuaskan**.
- Visualisasi data memberikan gambaran distribusi sentimen yang membantu dalam memahami opini pengunjung terhadap berbagai destinasi wisata di Bali.

## 🚀 How to Use
1. Clone repositori ini:
   ```bash
   git clone https://github.com/MuhIbrahimm/Sentiment-Analysis-of-Tourist-Attractions-in-Bali.git
   cd Sentiment-Analysis-of-Tourist-Attractions-in-Bali
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan skrip scrapping data:
   ```bash
   python [1]gmaps-review-scrapper.py
   ```
3. Jalankan skrip labelling data:
   ```bash
   python [2]pre_processing.py
   ```
3. Jalankan skrip pre-processing data:
   ```bash
   python [3]labelling-review.py
   ```
3. Jalankan skrip analisis sentimen:
   ```bash
   python [4]sentiment-analysis-MultinomialNB.py
   ```
5. Jalankan skrip visualisasi:
   ```bash
   python [5]visualization.py
   ```

## 📩 Contact
Jika ada pertanyaan atau saran, silakan buka issue di GitHub.

---
⭐ Jangan lupa untuk memberikan **star** pada repositori ini jika proyek ini bermanfaat. Terima kasih! ⭐

