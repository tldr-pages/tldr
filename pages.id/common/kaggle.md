# kaggle

> CLI resmi untuk Kaggle yang diimplementasikan dalam Python 3.
> Informasi lebih lanjut: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md>.

- Tampilkan nilai konfigurasi saat ini:

`kaggle config view`

- Unduh file tertentu dari dataset kompetisi:

`kaggle {{[c|competitions]}} download {{kompetisi}} {{[-f|--file]}} {{jalan/ke/file}}`

- Tampilkan daftar kompetisi yang sesuai dengan kata kunci pencarian:

`kaggle {{[c|competitions]}} list {{[-s|--search]}} {{kata_kunci}}`

- Tampilkan daftar file yang tersedia untuk kompetisi tertentu:

`kaggle {{[c|competitions]}} files {{kompetisi}}`

- Kirim file ke kompetisi disertai pesan:

`kaggle {{[c|competitions]}} submit {{kompetisi}} {{[-f|--file]}} {{jalan/ke/hasil_prediksi.csv}} {{[-m|--message]}} "{{pesan}}"`

- Tampilkan daftar dataset yang sesuai dengan kata kunci pencarian:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} {{kata_kunci}}`

- Unduh semua file dari sebuah dataset:

`kaggle {{[d|datasets]}} download {{pemilik}}/{{nama_dataset}}`

- Tampilkan daftar kernel (notebook) yang sesuai dengan kata kunci pencarian:

`kaggle {{[k|kernels]}} list {{[-s|--search]}} {{kata_kunci}}`
