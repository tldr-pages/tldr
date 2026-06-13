# afplay

> Program pemutar audio baris perintah.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- Putar suatu berkas audio (program menunggu hingga pemutaran selesai):

`afplay {{jalan/menuju/berkas}}`

- Putar audio dengan laju kecepatan 2 kali lipat:

`afplay --rate {{2}} {{jalan/menuju/berkas}}`

- Putar audio dengan laku kecepatan setengah kali lipat:

`afplay --rate {{0.5}} {{jalan/menuju/berkas}}`

- Hanya putar `n` (sekian) detik awal dari berkas audio:

`afplay --time {{n}} {{jalan/menuju/berkas}}`
