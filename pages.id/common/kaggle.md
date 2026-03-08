# kaggle

> CLI resmi untuk Kaggle yang diimplementasikan dalam Python 3.
> Informasi lebih lanjut: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md>.

- Tampilkan nilai konfigurasi saat ini:

`kaggle config view`

- Unduh berkas tertentu dari dataset kompetisi:

`kaggle {{[c|competitions]}} download {{nama_kompetisi}} {{[-f|--file]}} {{jalan/ke/berkas}}`

- Tampilkan daftar kompetisi yang sesuai dengan kata kunci pencarian:

`kaggle {{[c|competitions]}} list {{[-s|--search]}} {{kata_kunci_pencarian}}`

- Tampilkan daftar berkas yang tersedia untuk kompetisi tertentu:

`kaggle {{[c|competitions]}} files {{nama_kompetisi}}`

- Kirim sebuah berkas ke kompetisi dengan sebuah pesan:

`kaggle {{[c|competitions]}} submit {{nama_kompetisi}} {{[-f|--file]}} {{jalan/ke/berkas_kiriman.csv}} {{[-m|--message]}} "{{pesan}}"`

- Tampilkan daftar dataset yang sesuai dengan kata kunci pencarian:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} {{kata_kunci_pencarian}}`

- Unduh semua berkas dari sebuah dataset:

`kaggle {{[d|datasets]}} download {{pemilik}}/{{nama_dataset}}`

- Tampilkan daftar kernel (notebook) yang sesuai dengan kata kunci pencarian:

`kaggle {{[k|kernels]}} list {{[-s|--search]}} {{kata_kunci_pencarian}}`
