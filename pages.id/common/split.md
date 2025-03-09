# split

> Memisahkan sebuah file menjadi beberapa bagian.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>.

- Memisahkan sebuah file, tiap bagian memiliki 10 baris (kecuali di bagian terakhir):

`split -l 10 {{jalan/menuju/berkas}}`

- Memisahkan sebuah file menjadi 5 file. Dibagi sehingga masing-masing bagian memiliki ukuran yang sama (kecuali di bagian terakhir):

`split -n 5 {{jalan/menuju/berkas}}`

- Memisahkan sebuah file dengan ukuran 512 byte masing-masing bagiannya (kecuali di bagian terakhir; gunakan 512k untuk kilobyte dan 512m untuk megabytes):

`split -b 512 {{jalan/menuju/berkas}}`

- Memisahkan sebuah file dengan ukuran paling banyak 512 byte masing-masing bagiannya tanpa memotong baris:

`split -C 512 {{jalan/menuju/berkas}}`
