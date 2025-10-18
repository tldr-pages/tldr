# find

> Mencari file atau direktori di dalam sebuah struktur direktori (directory tree) secara rekursif.
> Informasi lebih lanjut: <https://manned.org/find>.

- Cari berkas berdasarkan ekstensi:

`find {{lokasi/awal}} -name '{{*.ext}}'`

- Cari berkas yang cocok dengan beberapa pola nama/lokasi:

`find {{lokasi/awal}} -path '{{*/lokasi/*/*.ext}}' -or -name '{{*pola*}}'`

- Cari direktori yang cocok dengan nama tertentu, dalam mode tidak peka huruf (case-insensitive):

`find {{lokasi/awal}} -type d -iname '{{*lib*}}'`

- Cari berkas yang cocok dengan pola tertentu, dengan mengecualikan lokasi spesifik:

`find {{lokasi/awal}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Cari berkas dengan rentang ukuran tertentu dengan membatasi kedalaman rekursif hingga "1":

`find {{lokasi/awal}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Jalankan perintah untuk setiap berkas/fail (gunakan `{}` di dalam perintah untuk mengakses nama berkas/fail):

`find {{lokasi/awal}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Cari semua berkas/fail yang diubah hari ini dan teruskan hasilnya sebagai argumen ke satu perintah:

`find {{lokasi/awal}} -daystart -mtime {{-1}} -exec {{tar -cvf arsip.tar}} {} \+`

- Cari berkas/fail atau direktori kosong lalu hapus dengan menampilkan prosesnya (verbose):

`find {{lokasi/awal}} -type {{f|d}} -empty -delete -print`
