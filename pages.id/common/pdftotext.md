# pdftotext

> Konversi berkas PDF ke format teks murni (plain text).
> Informasi lebih lanjut: <https://www.xpdfreader.com/pdftotext-man.html>.

- Konversi `nama_berkas.pdf` ke teks murni dan cetak ke `stdout`:

`pdftotext {{nama_berkas.pdf}} -`

- Konversi `nama_berkas.pdf` ke teks murni dan simpan sebagai `nama_berkas.txt`:

`pdftotext {{nama_berkas.pdf}}`

- Konversi `nama_berkas.pdf` ke teks murni dengan tetap mempertahankan tata letak (layout):

`pdftotext -layout {{nama_berkas.pdf}}`

- Konversi `berkas_masukan.pdf` ke teks murni dan simpan sebagai `berkas_keluaran.txt`:

`pdftotext {{berkas_masukan.pdf}} {{berkas_keluaran.txt}}`

- Konversi halaman 2, 3, dan 4 dari `berkas_masukan.pdf` ke teks murni dan simpan sebagai `berkas_keluaran.txt`:

`pdftotext -f {{2}} -l {{4}} {{berkas_masukan.pdf}} {{berkas_keluaran.txt}}`
