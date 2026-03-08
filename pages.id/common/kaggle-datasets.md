# kaggle datasets

> Mengelola dataset Kaggle.
> Informasi lebih lanjut: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>.

- Tampilkan semua dataset milik pengguna atau organisasi tertentu:

`kaggle {{[d|datasets]}} list --user {{nama_pengguna}}`

- Cari dataset berdasarkan nama:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} "{{nama_dataset}}"`

- Unduh sebuah dataset:

`kaggle {{[d|datasets]}} download "{{nama_dataset}}"`

- Buat sebuah dataset publik:

`kaggle {{[d|datasets]}} create {{[-p|--path]}} {{jalan/ke/dataset}} {{[-u|--public]}}`

- Unduh metadata dari sebuah dataset:

`kaggle {{[d|datasets]}} metadata {{nama_dataset}}`

- Inisialisasi metadata untuk sebuah dataset:

`kaggle {{[d|datasets]}} init {{[-p|--path]}} {{jalan/ke/dataset}}`

- Hapus sebuah dataset:

`kaggle {{[d|datasets]}} delete {{nama_dataset}}`
