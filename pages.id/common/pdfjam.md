# pdfjam

> Antarmuka baris perintah (shell frontend) untuk paket LaTeX pdfpages guna mengolah berkas-berkas PDF.
> Informasi lebih lanjut: <https://github.com/pdfjam/pdfjam/blob/master/doc/pdfjam-help.txt>.

- Gabungkan dua (atau lebih) berkas PDF:

`pdfjam {{jalan/ke/berkas1.pdf jalan/ke/berkas2.pdf ...}} {{[-o|--outfile]}} {{jalan/ke/berkas_keluaran.pdf}}`

- Gabungkan halaman pertama dari setiap berkas menjadi satu:

`pdfjam {{jalan/ke/berkas1.pdf 1 jalan/ke/berkas2.pdf 1 ...}} {{[-o|--outfile]}} {{jalan/ke/berkas_keluaran.pdf}}`

- Gabungkan sub-rentang (subrange) halaman dari dua berkas PDF:

`pdfjam {{jalan/ke/berkas1.pdf 3-5,1}} {{jalan/ke/berkas2.pdf 4-6}} {{[-o|--outfile]}} {{jalan/ke/berkas_keluaran.pdf}}`

- Tandatangani halaman A4 (sesuaikan nilai delta dengan tinggi untuk format lain) dengan tanda tangan pindaian (scan) dengan cara menumpuknya:

`pdfjam {{jalan/ke/berkas.pdf}} {{jalan/ke/tanda_tangan}} --fitpaper true {{[-o|--outfile]}} {{jalan/ke/berkas_tertanda.pdf}} --nup "{{1x2}}" --delta "{{0 -842pt}}"`

- Atur halaman-halaman dari berkas masukan ke dalam kisi (grid) 2x2:

`pdfjam {{jalan/ke/berkas.pdf}} --nup {{2x2}} --suffix {{4up}} --preamble '{{\usepackage{fancyhdr} \pagestyle{fancy}}}'`

- Balikkan urutan halaman di dalam setiap berkas yang diberikan dan gabungkan mereka:

`pdfjam {{jalan/ke/berkas1.pdf last-1 jalan/ke/berkas2.pdf last-1 ...}} --suffix {{reversed}}`
