# asciinema

> Rekam dan putar ulang sesi terminal, dan secara opsional membagikannya di <https://asciinema.org>.
> Lihat juga: `terminalizer`.
> Informasi lebih lanjut: <https://docs.asciinema.org/manual/cli/>.

- Masuk dengan suatu akun asciinema.org:

`asciinema auth`

- Buat rekaman baru (hentikan dengan `<Ctrl d>` atau ketik `exit`, kemudian pilih lokasi penyimpanan baik dengan mengunggah atau menyimpannya secara lokal):

`asciinema rec`

- Buat rekaman baru kemudian simpan ke dalam suatu berkas lokal:

`asciinema rec {{jalan/menuju/rekaman.cast}}`

- Putar ulang rekaman sesi terminal dari suatu berkas lokal:

`asciinema play {{jalan/menuju/rekaman.cast}}`

- Putar ulang suatu rekaman sesi terminal yang dipublikasikan di <https://asciinema.org>:

`asciinema play https://asciinema.org/a/{{id_rekaman}}`

- Buat rekaman baru, dengan membatasi waktu diam/idle terlama selama 2.5 detik:

`asciinema rec {{[-i|--idle-time-limit]}} 2.5`

- Tampilkan seluruh luaran/output terminal yang dikeluarkan selama sesi perekaman:

`asciinema cat {{jalan/menuju/rekaman.cast}}`

- Unggah suatu berkas hasil rekaman lokal menuju asciinema.org:

`asciinema upload {{jalan/menuju/rekaman.cast}}`
