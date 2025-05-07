# Predict New York Yellow Taxi Price

## Repository Outline
`Pada project ini mempunyai 9 file`

```
1. README.md - Penjelasan gambaran umum project
2. P1M2_Reido_Vidaya.ipynb - Notebook yang berisi pengolahan data dengan python
3. P1M2_Reido_Vidaya_inf.ipynb - Notebook yang berisi model inference
4. taxi.csv - Dataset yang digunakan untuk pengolahan data
5. model.pkl - Model yang telah dibuat untuk prediksi
6. EDA.py - Program yang dibuat untuk menampilkan EDA pada streamlit
7. prediction.py - Program yang dibuat untuk prediksi harga taxi
8. app.py - Program untama yang mengintegrasikan EDA.py dan prediction.py
9. url.txt - Berisi url dataset dan url deploy

```

## Problem Background
`Pada project ini bertujuan untuk membuat model machine learning yang dapat memprediksi harga taksi berdasarkan fitur yang tersedia. Harga taxi dipengaruhi oleh beberapa faktor salah satunya jarak. Oleh karena itu memprediksi harga taksi secara akurat akan sangat berguna terutama dalam industri transportasi.`

## Project Output
`Output dari project ini adalah model machine learning yang berhasil memprediksi harga taksi`

## Data
`Data yang digunakan dalam project ini diperoleh dari BigQuery. Terdapat 12 kolom dan 10000 baris `

```
1. Vendor_id - Penyedia sistem pencatatan perjalanan dan pembayaran
2. dropoff_datetime - Waktu ketika pencatatan aktif
3. rate_code - Kode tarif berdasarkan tujuan
4. passenger_count - Banyaknya penumpang pada taksi
5. trip_distance - Jarak perjalanan dalam mil
6. payment_type - Jenis pembayaran
7. fare_amount - Tarif berdasarkan waktu dan jarak
8. extra - Biaya tambahan
9. tip_amount - Jumlah tip
10. tolls_amount - Tarif tol per trip
11. imp_surcharge - Biaya tambahan yang diterapkan sejak tahun 2005
12. total_amount - Total tarif taksi
```

## Method
`Metode yang digunakan dalam project ini adalah Random Forest yang merupakan salah satu metode supervised learning. Random Forest bekerja dengan membangun pohon keputusan yang besar kemudian menggabungkan hasil dari setiap pohon tersebut`

## Stacks
`Project ini menggunakan bahasa pemrogaman python dengan beberapa library dibawah ini :`

```
- Pandas untuk manipulasi data
- NumPy untuk operasi matematis dan array
- Mathplotlib dan seaborn untuk visualisasi data
- Scikit-learn untuk implementasi model machine learning
- Pickle untuk menyimpan dan memuat model machine learning
- Phik untuk menghitung korelasi antar fitur
- Feature_engine.outliers untuk menangani data outlier
```

## Reference
`Link Hugging Face : https://huggingface.co/spaces/reido2000/Milestone `
