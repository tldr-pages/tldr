# ani-cli

> Program baris perintah (CLI) untuk menelusuri dan menonton film anime.
> Lihat juga: `animdl`.
> Informasi lebih lanjut: <https://manned.org/ani-cli>.

- Cari konten anime dengan nama:

`ani-cli "{{judul_anime}}"`

- Unduh konten suatu episode:

`ani-cli {{[-d|--download]}} "{{judul_anime}}"`

- Unduh konten suatu rentang episode:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{judul_anime}}"`

- Unduh konten suatu seri (rangkaian dari seluruh episode) secara menyeluruh:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{judul_anime}}"`

- Gunakan VLC untuk memutar film:

`ani-cli {{[-v|-vlc]}} "{{judul_anime}}"`

- Tonton suatu [e]pisode:

`ani-cli {{[-e|--episode]}} {{nomor_episode}} "{{judul_anime}}"`

- Lanjut menonton anime dari riwayat:

`ani-cli {{[-c|--continue]}}`

- Mutakhirkan program `ani-cli`:

`ani-cli {{[-U|--update]}}`
