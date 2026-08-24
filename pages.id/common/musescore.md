# musescore

> Program pengolah lembaran musik MuseScore.
> Lihat juga: `lilypond`.
> Informasi lebih lanjut: <https://handbook.musescore.org/appendix/command-line-usage>.

- Tentukan besaran arus bitrate dalam kbit/s:

`musescore {{[-b|--bitrate]}} {{bitrate}}`

- Jalankan MuseScore dalam mode awakutu (debug):

`musescore {{[-d|--debug]}}`

- Nyalakan fitur percobaan, seperti manipulasi layer audio:

`musescore {{[-e|--experimental]}}`

- Ekspor suatu berkas ke dalam berkas output yang ditentukan. Jenis format berkas ditentukan berdasarkan nama ekstensi:

`musescore {{[-o|--export-to]}} {{berkas_luaran}} {{berkas_masukan}}`

- Tampilkan perbedaan isi antara kedua berkas skor musik:

`musescore --diff {{jalan/menuju/berkas1}} {{jalan/menuju/berkas2}}`

- Gunakan suatu berkas konfigurasi impor untuk MIDI:

`musescore {{[-M|--midi-operations]}} {{jalan/menuju/berkas}}`
