# kaggle kernels

> Kelola kernel-kernel Kaggle.
> Informasi lebih lanjut: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#kernels>.

- Tampilkan daftar semua kernel:

`kaggle {{[k|kernels]}} list`

- Tampilkan daftar file output dari sebuah kernel:

`kaggle {{[k|kernels]}} files {{nama_kernel}}`

- Inisialisasi file metadata untuk sebuah kernel (secara default ke direktori saat ini):

`kaggle {{[k|kernels]}} init {{[-p|--path]}} {{jalan/ke/direktori}}`

- Unggah kode baru ke sebuah kernel dan jalankan kernel tersebut:

`kaggle {{[k|kernels]}} push {{[-p|--path]}} {{jalan/ke/direktori}}`

- Unduh sebuah kernel:

`kaggle {{[k|kernels]}} pull {{nama_kernel}} {{[-p|--path]}} {{jalan/ke/direktori}}`

- Dapatkan output data dari eksekusi kernel terakhir:

`kaggle {{[k|kernels]}} output {{nama_kernel}}`

- Tampilkan status dari eksekusi kernel terakhir:

`kaggle {{[k|kernels]}} status {{nama_kernel}}`
