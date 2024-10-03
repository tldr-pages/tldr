# comp

> Bandingkan isi antar kedua berkas atau himpunan berkas.
> Gunakan wildcard (*) untukk membandingkan himpunan berkas.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- Bandingkan isi berkas secara interaktif:

`comp`

- Bandingkan isi antara kedua berkas:

`comp {{jalan\menuju\berkas1}} {{jalan\menuju\berkas2}}`

- Bandingkan isi antara kedua himpunan berkas:

`comp {{jalan\menuju\direktori1}}\* {{jalan\menuju\direktori2}}\*`

- Tampilkan perbedaan dalam format [d]esimal:

`comp /d {{jalan\menuju\berkas1}} {{jalan\menuju\berkas2}}`

- Tampilkan perbedaan dalam format [a]SCII:

`comp /a {{jalan\menuju\berkas1}} {{jalan\menuju\berkas2}}`

- Tampilkan nomor baris di mana perbedaan antar isi terdeteksi:

`comp /l {{jalan\menuju\berkas1}} {{jalan\menuju\berkas2}}`

- Bandingkan berkas-berkas tanpa menghiraukan penggunaan huruf besar/kecil ([c]ase-insensitive):

`comp /c {{jalan\menuju\berkas1}} {{jalan\menuju\berkas2}}`

- Hanya bandingkan isi 5 baris pertama antara kedua berkas:

`comp /n=5 {{jalan\menuju\berkas1}} {{jalan\menuju\berkas2}}`
