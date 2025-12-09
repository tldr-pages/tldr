# animdl

> Suatu mesin scraper konten anime secara efisien, kuat, dan cepat.
> Lihat juga: `ani-cli`.
> Informasi lebih lanjut: <https://github.com/justfoolingaround/animdl>.

- Unduh konten suatu anime:

`animdl download {{judul_anime}}`

- Unduh konten anime dalam rentang episode:

`animdl download {{judul_anime}} {{[-r|--range]}} {{episode_awal}}-{{episode_akhir}}`

- Unduh konten anime ke dalam suatu direktori tertentu:

`animdl download {{judul_anime}} {{[-d|--download-dir]}} {{jalan/menuju/direktori_hasil_unduhan}}`

- Ambil URL untuk menayangkan suatu judul anime:

`animdl grab {{judul_anime}}`

- Dapatkan jadwal tayang anime untuk satu minggu ke depan:

`animdl schedule`

- Cari konten untuk suatu judul anime:

`animdl search {{judul_anime}}`

- Tayangkan konten suatu judul anime:

`animdl stream {{judul_anime}}`

- Tayangkan episode terkini untuk suatu judul anime:

`animdl stream {{judul_anime}} {{[-s|--special]}} latest`
