# kaggle kernels

> Mengelola kernel Kaggle.
> Informasi lebih lanjut: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#kernels>.

- Tampilkan daftar semua kernel:

`kaggle {{[k|kernels]}} list`

- Tampilkan daftar berkas keluaran (output) kernel:

`kaggle {{[k|kernels]}} files {{nama_kernel}}`

- Inisialisasi berkas metadata untuk sebuah kernel (secara baku ke direktori saat ini):

`kaggle {{[k|kernels]}} init {{[-p|--path]}} {{jalan/ke/direktori}}`

- Kirim (push) kode baru ke sebuah kernel dan jalankan kernel tersebut:

`kaggle {{[k|kernels]}} push {{[-p|--path]}} {{jalan/ke/direktori}}`

- Ambil (pull) sebuah kernel:

`kaggle {{[k|kernels]}} pull {{nama_kernel}} {{[-p|--path]}} {{jalan/ke/direktori}}`

- Dapatkan data keluaran dari eksekusi kernel terbaru:

`kaggle {{[k|kernels]}} output {{nama_kernel}}`

- Tampilkan status dari eksekusi kernel terbaru:

`kaggle {{[k|kernels]}} status {{nama_kernel}}`
