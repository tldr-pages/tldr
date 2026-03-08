# pdfgrep

> Mencari teks di dalam berkas PDF.
> Informasi lebih lanjut: <https://pdfgrep.org/doc.html>.

- Temukan baris-baris yang cocok dengan pola tertentu dalam berkas PDF:

`pdfgrep {{pola}} {{berkas.pdf}}`

- Sertakan nama berkas dan nomor halaman untuk setiap baris yang cocok:

`pdfgrep {{[-H|--with-filename]}} {{[-n|--page-number]}} {{pola}} {{berkas.pdf}}`

- Lakukan pencarian yang tidak peka huruf besar-kecil (case-insensitive) untuk baris yang diawali dengan nama_berkas dan kembalikan 3 kecocokan pertama:

`pdfgrep {{[-m|--max-count]}} {{3}} {{[-i|--ignore-case]}} '{{^nama_berkas}}' {{berkas.pdf}}`

- Temukan pola dalam berkas-berkas dengan ekstensi .pdf di direktori saat ini secara rekursif:

`pdfgrep {{[-r|--recursive]}} {{pola}}`

- Temukan pola pada berkas yang cocok dengan pola glob tertentu di direktori saat ini secara rekursif:

`pdfgrep {{[-r|--recursive]}} --include '{{*buku.pdf}}' {{pola}}`
