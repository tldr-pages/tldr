# bun add

> Alat runtime, manajer paket, pengemas, dan penguji program JavaScript mutakhir.
> Catatan: `a` dapat dipakai sebagai alias bagi `add`.
> Informasi lebih lanjut: <https://bun.com/docs>.

- Pasang sebuah paket:

`bun add {{paket}}`

- Pasang beberapa paket:

`bun add {{paket1 paket2 ...}}`

- Pasang suatu paket dari repositori Git:

`bun add {{url_git}}`

- Pasang paket dengan versi tertentu:

`bun add {{paket}}@{{versi}}`

- Pasang paket dari suatu berkas atau direktori lokal:

`bun add file:{{jalan/menuju/berkas_atau_direktori}}`

- Tambahkan paket sebagai ketergantungan untuk membangun program saja (dev dependency):

`bun add {{[-d|--dev]}} {{paket}}`

- Tambahkan paket menuju lingkungan runtime global:

`bun add {{[-g|--global]}} {{paket}}`
