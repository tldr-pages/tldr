# pdftk

> Perangkat perkakas (toolkit) PDF.
> Informasi lebih lanjut: <https://www.pdflabs.com/docs/pdftk-man-page/>.

- Ekstrak halaman 1-3, 5, dan 6-10 dari sebuah berkas PDF dan simpan sebagai berkas baru:

`pdftk {{jalan/ke/berkas_masukan}}.pdf cat 1-3 5 6-10 output {{jalan/ke/berkas_keluaran}}.pdf`

- Gabungkan (gabung berturutan) daftar berkas PDF dan simpan hasilnya sebagai berkas baru:

`pdftk {{jalan/ke/berkas1}}.pdf {{jalan/ke/berkas2}}.pdf cat output {{jalan/ke/berkas_keluaran}}.pdf`

- Pecah setiap halaman berkas PDF menjadi berkas-berkas terpisah, dengan pola nama berkas keluaran tertentu:

`pdftk {{jalan/ke/berkas_masukan}}.pdf burst output {{jalan/ke/keluaran_%d}}.pdf`

- Putar semua halaman sebesar 180 derajat searah jarum jam:

`pdftk {{jalan/ke/berkas_masukan}}.pdf cat 1-endsouth output {{jalan/ke/berkas_keluaran}}.pdf`

- Putar halaman ketiga sebesar 90 derajat searah jarum jam dan biarkan halaman lainnya tidak berubah:

`pdftk {{jalan/ke/berkas_masukan}}.pdf cat 1-2 3east 4-end output {{jalan/ke/berkas_keluaran}}.pdf`

- Selipkan (interleave) halaman-halaman dari dua PDF yang berisi hasil pemindaian satu sisi dari dokumen dua sisi, di mana bagian belakang dipindai dari belakang ke depan:

`pdftk A={{jalan/ke/halaman_depan}}.pdf B={{jalan/ke/halaman_belakang}}.pdf shuffle A1-end Bend-1 output {{jalan/ke/berkas_keluaran}}.pdf`
