# asciinema

> Rekam dan putar ulang sesi terminal, dan secara opsional membagikannya di <https://asciinema.org>.
> Lihat juga: `terminalizer`, `agg`.
> Informasi lebih lanjut: <https://docs.asciinema.org/manual/cli/>.

- Masuk dengan suatu akun asciinema.org:

`asciinema {{[a|auth]}}`

- Buat rekaman baru (hentikan dengan `<Ctrl d>` atau ketik `exit`, kemudian pilih lokasi penyimpanan baik dengan mengunggah atau menyimpannya secara lokal):

`asciinema {{[r|record]}} {{jalan/menuju/rekaman.cast}}`

- Putar ulang rekaman sesi terminal dari suatu berkas lokal:

`asciinema {{[p|play]}} {{jalan/menuju/rekaman.cast}}`

- Putar ulang suatu rekaman sesi terminal yang dipublikasikan di <https://asciinema.org>:

`asciinema {{[p|play]}} https://asciinema.org/a/{{id_rekaman}}`

- Buat rekaman baru, dengan membatasi waktu diam/idle terlama selama 2.5 detik:

`asciinema {{[r|record]}} {{[-i|--idle-time-limit]}} 2.5`

- Tampilkan seluruh luaran/output terminal yang dikeluarkan selama sesi perekaman:

`asciinema {{[ca|cat]}} {{jalan/menuju/rekaman.cast}}`

- Unggah suatu berkas hasil rekaman lokal menuju asciinema.org:

`asciinema {{[u|upload]}} {{jalan/menuju/rekaman.cast}}`

- Siarkan terminal saat ini dalam sebuah situs web lokal:

`asciinema {{[st|stream]}} --local`
