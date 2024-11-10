# mv

> Pindahkan atau namai-ulang berkas dan direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/mv>.

- Pindahkan berkas ke lokasi yang baru:

`mv {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Pindahkan berkas atau direktori ke dalam direktori lain yang telah ada:

`mv {{jalan/menuju/sumber}} {{jalan/menuju/direktori}}`

- Pindahkan berkas majemuk ke dalam direktori lain yang telah ada, dengan menyimpan nama masing-masing file secara utuh:

`mv {{jalan/menuju/sumber1 jalan/menuju/sumber2 ...}} {{jalan/menuju/direktori}}`

- Pindahkan tanpa meminta konfirmasi sebelum menimpa file yang sudah ada:

`mv -f {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Minta konfirmasi sebelum menimpa berkas yang sudah ada, tanpa memerhatikan hak akses hedua file tersebut:

`mv -i {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Jangan menimpa file yang sudah ada di direktori tujuan:

`mv -n {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Pindahkan berkas dalam mode [v]erbose, tampilkan berkas-berkas yang dipindahkan:

`mv -v {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`
