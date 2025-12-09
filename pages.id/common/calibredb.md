# calibredb

> Kelola suatu pangkalan data perpustakaan buku digital.
> Bagian dari aplikasi perpustakaan buku digital Calibre.
> Informasi lebih lanjut: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- Tampilkan daftar judul dan informasi tambahan terkait buku-buku digital yang telah terdaftar dalam perpustakaan:

`calibredb list`

- Cari kumpulan buku dengan informasi tambahan:

`calibredb list --search {{kata_kunci}}`

- Hanya tampilkan nomor induk (id) dari hasil pustaka pencarian:

`calibredb search {{kata_kunci}}`

- Masukkan satu atau beberapa buku baru ke dalam perpustakaan:

`calibredb add {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Masukkan seluruh buku dalam suatu direktori secara rekursif:

`calibredb add {{[-r|--recurse]}} {{jalan/menuju/direktori}}`

- Hapus satu atau beberapa buku dari perpustakaan. Anda perlu memasukkan nomor-nomor induk (lihat keterangan di atas):

`calibredb remove {{id1 id2 ...}}`
