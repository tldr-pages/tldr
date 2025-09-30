# mv

> Pindahkan atau namai-ulang berkas dan direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Pindahkan berkas ke lokasi yang baru:

`mv {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Pindahkan berkas atau direktori ke dalam direktori lain yang telah ada:

`mv {{jalan/menuju/sumber}} {{jalan/menuju/direktori}}`

- Pindahkan berkas majemuk ke dalam direktori lain yang telah ada, dengan menyimpan nama masing-masing file secara utuh:

`mv {{jalan/menuju/sumber1 jalan/menuju/sumber2 ...}} {{jalan/menuju/direktori}}`

- Pindahkan tanpa meminta konfirmasi sebelum menimpa file yang sudah ada:

`mv {{[-f|--force]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Minta konfirmasi sebelum menimpa berkas yang sudah ada, tanpa memerhatikan hak akses hedua file tersebut:

`mv {{[-i|--interactive]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Jangan menimpa file yang sudah ada di direktori tujuan:

`mv {{[-n|--no-clobber]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Pindahkan berkas dalam mode verbose, tampilkan berkas-berkas yang dipindahkan:

`mv {{[-v|--verbose]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Tetapkan direktori tujuan target agar Anda dapat menggunakan alat atau perintah eksternal untuk mengelola kumpulan berkas yang dapat dipindahkan:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{jalan/menuju/direktori_tujuan}}`
