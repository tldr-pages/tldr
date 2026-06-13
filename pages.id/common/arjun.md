# arjun

> Temukan parameter HTTP yang tersedia untuk sistem aplikasi web.
> Informasi lebih lanjut: <https://github.com/s0md3v/Arjun/wiki/Usage>.

- Pindai suatu URL untuk mendapatkan parameter GET yang tersedia:

`arjun -u {{https://example.com/page.php}}`

- Pindai menggunakan metode permintaan POST:

`arjun -u {{https://example.com/api}} -m POST`

- Simpan hasil pemindaian ke dalam suatu berkas JSON:

`arjun -u {{https://example.com}} -o {{jalan/menuju/luaran.json}}`

- Gunakan berkas daftar kata (wordlist) tertentu untuk memindai:

`arjun -u {{https://example.com}} -w {{jalan/menuju/daftar_kata.txt}}`

- Perbesar jumlah detik waktu tunggu antar permintaan untuk menghindari pembatasan laju permintaan:

`arjun -u {{https://example.com}} -d {{2}}`
