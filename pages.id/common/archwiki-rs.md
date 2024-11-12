# archwiki-rs

> Baca, cari, dan unduh artikel dari situs ArchWiki.
> Informasi lebih lanjut: <https://gitlab.com/lucifayr/archwiki-rs>.

- Baca suatu artikel dari situs ArchWiki:

`archwiki-rs read-page {{judul_artikel}}`

- Baca suatu artikel dari ArchWiki dengan format tertentu:

`archwiki-rs read-page {{judul_artikel}} --format {{plain-text|markdown|html}}`

- Cari artikel dalam ArchWiki yang mengandung teks tertentu:

`archwiki-rs search "{{teks_yang_dicari}}" --text-search`

- Unduh seluruh artikel dari situs ArchWiki ke dalam suatu direktori:

`archwiki-rs local-wiki {{/jalan/menuju/wiki_lokal}} --format {{plain-text|markdown|html}}`
