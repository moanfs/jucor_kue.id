# Klasifikasi Kue Tradisional Indonesia Menggunakan Algoritma CNN dan VisionTransformer
*Proyek Akhir MBKM Orbit

Anggota Kelompok:

Halomoan Filipus Simarmata (Jupyter XXI)
Diana Eka Riyani (Jupyter XXI)
Nyayu Chika Marselina (Jupyter XXI)
Sukma Imelda (Cordoba)
Athiya Shinta Wulandari (Cordoba)

# AI Project Cycle (Computer Vision)

# Problem Solving
What? (Apa masalahnya? Apa yg dibutuhkan?) : Banyaknya masyarakat yang tidak memakai masker saat pandemi sehingga dibutuhkannya pendeteksi masker wajah untuk menghindari penyebaran kasus COVID-19 dan juga meminimalisir pelanggaran protokol kesehatan yang sudah ditetapkan oleh pemerintah.
Where? (Dimana / pada saat apa permasalahan ini muncul?) : Di tempat umum yang memungkinkan untuk berinteraksi dengan orang lain (di luar tempat tinggal). Masalah ini muncul pada saat era pandemi COVID-19.
Who? (Stakeholder yang terkait) : Masyarakat
Why? (Kenapa masalah ini muncul? Bagaimana solusinya?) : Pendeteksi penggunaan masker dianggap penting apalagi di masa pandemi seperti sekarang dikarenakan banyaknya masyarakat yang masih tidak mengenakan masker saat berada di luar ruangan atau saat berinteraksi dengan orang lain sehingga membuatnya bisa saja terindikasi virus COVID-19.

# Data Acquisition
Data diperoleh dari github (https://github.com/Soedirman-Machine-Learning/face-mask-detection) dengan data sebanyak 350 gambar yang kelompok kami olah dari data asli sebanyak 4500 data.

# Data Exploration
Data berupa kumpulan foto orang yang mengenakan masker dan yang tidak mengenakan masker.

# Modelling
Program dalam Mini Project ini menggunakan  algoritma CNN (Convolutional Neural Network) dan algoritma VisionTransformer.

# Evaluation
Dari pengolahan data yang kami lakukan seperti:
1. Extrasi gambar
2. Mengkonversi data ke dalam Numpy Array
3. Split data
4. Pelatihan Model
5. Dan lain-lain
Kami mendapat akurasi 100%, dari hasil akurasi tersebut memungkinkan dapat terjadinya overfitting tetapi dari hasil plot confusion matrix tidak ada kesalahan data. Mungkin bisa terjadi akibat data yang kami gunakan hanya sekitar -+8% dari data aslinya.
