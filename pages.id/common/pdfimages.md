# pdfimages

> Utilitas untuk mengekstrak gambar dari berkas PDF.
> Informasi lebih lanjut: <https://manned.org/pdfimages>.

- Ekstrak semua gambar dari sebuah berkas PDF dan simpan sebagai berkas PNG:

`pdfimages -png {{jalan/ke/berkas.pdf}} {{awalan_nama_berkas}}`

- Ekstrak gambar dari halaman 3 sampai 5:

`pdfimages -f {{3}} -l {{5}} {{jalan/ke/berkas.pdf}} {{awalan_nama_berkas}}`

- Ekstrak gambar dari sebuah berkas PDF dan sertakan nomor halaman pada nama berkas keluaran:

`pdfimages -p {{jalan/ke/berkas.pdf}} {{awalan_nama_berkas}}`

- Tampilkan daftar informasi tentang semua gambar dalam sebuah berkas PDF:

`pdfimages -list {{jalan/ke/berkas.pdf}}`
