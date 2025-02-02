from pymongo import MongoClient
import pandas as pd

# Menghubungkan ke MongoDB
client = MongoClient('YOUR_MONGODB_CONNECTION_STRING')
db = client['YOUR_DATABASE']
collection = db['YOUR_COLLECTION']

# Mengambil data dari MongoDB ke dalam DataFrame
data = list(collection.find())
df = pd.DataFrame(data)

# Fungsi untuk meminta input pengguna
def label_review():
    while True:
        try:
            label = int(input("(1=positif, 2=netral, 3=negatif, 4=skip, 0=berhenti): "))
            if label == 1:
                return 'positif'
            elif label == 2:
                return 'netral'
            elif label == 3:
                return 'negatif'
            elif label == 4:
                return 'skip'
            elif label == 0:
                return 'berhenti'
            else:
                print("Input tidak valid. Masukkan angka 1, 2, 3, 4, atau 0.")
        except ValueError:
            print("Input tidak valid. Masukkan angka 1, 2, 3, 4, atau 0.")

# Fungsi untuk menghitung jumlah label
def count_labels():
    print("===============================================================")
    if 'label' in df.columns:
        counts = df['label'].value_counts().to_dict()
        print("Jumlah data yang sudah dilabeli:")
        print(f"Positif: {counts.get('positif', 0)}")
        print(f"Netral: {counts.get('netral', 0)}")
        print(f"Negatif: {counts.get('negatif', 0)}")
    else:
        print("Jumlah data yang sudah dilabeli:")
        print("Positif: 0")
        print("Netral: 0")
        print("Negatif: 0")
    print("===============================================================")

# Fungsi untuk memilih tempat wisata
def select_place_name():
    places = df['Place Name'].unique()
    print("Daftar Tempat Wisata:")
    for i, place in enumerate(places):
        print(f"{i+1}. {place}")
    
    while True:
        try:
            choice = int(input("Pilih nomor tempat wisata yang ingin Anda lihat review-nya: "))
            if 1 <= choice <= len(places):
                return places[choice - 1]
            else:
                print("Pilihan tidak valid. Masukkan nomor yang sesuai.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor yang sesuai.")

# Fungsi utama untuk menampilkan review berdasarkan tempat wisata
def display_reviews_by_place():
    selected_place = select_place_name()
    reviews_by_place = df[(df['Place Name'] == selected_place) & 
                          (df['Review Rating'].isin(['1 bintang', '2 bintang']))] #untuk rating
    
    if reviews_by_place.empty:
        print(f"Tidak ada review untuk tempat wisata '{selected_place}'.\n")
        return

    for i, row in reviews_by_place.iterrows():
        if 'label' not in row or pd.isnull(row['label']):
            count_labels()
            print(f"Review untuk tempat wisata '{selected_place}': \n{row['Review Text']}")
            print("===============================================================")
            label = label_review()
            if label == 'berhenti':
                break
            elif label == 'skip':
                continue  # Skip ke data selanjutnya
            elif label in ['positif', 'netral', 'negatif']:
                df.at[i, 'label'] = label
                collection.update_one({'_id': row['_id']}, {'$set': {'label': label}})
                print(f"Label '{label}' Tersimpan untuk tempat wisata '{selected_place}'")
                print("===============================================================")

    print("Program berhenti. Data yang sudah dilabeli tersimpan dalam MongoDB.")

# Menampilkan review berdasarkan tempat wisata tertentu
display_reviews_by_place()
