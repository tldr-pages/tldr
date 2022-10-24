# split

> Memisahkan sebuah file menjadi beberapa bagian.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/split>.

- Memisahkan sebuah file, tiap bagian memiliki 10 baris (kecuali di bagian terakhir):

`split -l {{10}} {{nama_file}}`

- Memisahkan sebuah file menjadi 5 file. Dibagi sehingga masing-masing bagian memiliki ukuran yang sama (kecuali di bagian terakhir):

`split -n {{5}} {{nama_file}}`

- Memisahkan sebuah file dengan ukuran 512 byte masing-masing bagiannya (kecuali di bagian terakhir; gunakan 512k untuk kilobyte dan 512m untuk megabytes):

`split -b {{512}} {{nama_file}}`

- Memisahkan sebuah file dengan ukuran paling banyak 512 byte masing-masing bagiannya tanpa memotong baris:

`split -C {{512}} {{nama_file}}`
