# autopep8

> Tulis ulang kode Python dalam standar format pengayaan kode PEP 8.
> Informasi lebih lanjut: <https://github.com/hhatto/autopep8>.

- Coba tulis ulang kode suatu berkas menuju `stdout` dengan menentukan panjang baris maksimum:

`autopep8 {{jalan/menuju/berkas.py}} --max-line-length {{length}}`

- Coba tulis ulang suatu berkas, dan tampilkan daftar perbedaan isi berkas (diff):

`autopep8 --diff {{jalan/menuju/berkas}}`

- Tulis dan langsung sunting ulang suatu berkas:

`autopep8 --in-place {{jalan/menuju/berkas.py}}`

- Tulis dan langsung sunting ulang seluruh berkas dalam suatu direktori secara rekursif:

`autopep8 --in-place --recursive {{jalan/menuju/direktori}}`
