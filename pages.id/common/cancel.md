# cancel

> Batalkan penugasan pencetakan dokumen terhadap mesin-mesin pencetak (printer).
> Lihat juga: `lp`, `lpmove`, `lpstat`.
> Informasi lebih lanjut: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- Batalkan pekerjaan yang sedang dikerjakan ke dalam mesin pencetak yang diatur sebagai tujuan bawaan (atur mesin tujuan bawaan dengan perintah `lpoptions -d {{pencetak}}`):

`cancel`

- Batalkan pekerjaan yang sedang dikerjakan ke dalam mesin pencetak yang diatur sebagai tujuan bawaan menurut pengaturan suatu pengguna ([u]ser):

`cancel -u {{username}}`

- Batalkan pekerjaan yang sedang dikerjakan ke dalam suatu mesin pencetak:

`cancel {{pencetak}}`

- Batalkan suatu pekerjaan yang sedang dikerjakan ke dalam suatu mesin pencetak:

`cancel {{pencetak}}-{{nomor_induk_pekerjaan}}`

- Batalkan semu[a] pekerjaan yang sedang dan akan dikerjakan oleh mesin pencetak apapun:

`cancel -a`

- Batalkan semu[a] pekerjaan yang sedang dan akan dikerjakan oleh suatu mesin pencetak:

`cancel -a {{pencetak}}`

- Batalkan pekerjaan yang sedang ditangani oleh suatu peladen (server) layanan pencetak, kemudian hapus ([x]) berkas-berkas data pendukung pekerjaan:

`cancel -h {{peladen}} -x`
