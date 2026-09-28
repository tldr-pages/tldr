# firefox

> Suatu peramban web gratis dan bersumber terbuka.
> Informasi lebih lanjut: <https://wiki.mozilla.org/Firefox/CommandLineOptions>.

- Jalankan Firefox dan buka suatu laman web:

`firefox {{https://www.duckduckgo.com}}`

- Buka jendela aplikasi baru:

`firefox --new-window {{https://www.duckduckgo.com}}`

- Buka jendela peramban privat (incognito):

`firefox --private-window`

- Cari untuk "wikipedia" menggunakan pilihan mesin pencari bawaan:

`firefox --search "{{wikipedia}}"`

- Jalankan Firefox dalam mode aman, dengan seluruh add-on dimatikan:

`firefox --safe-mode`

- Ambil tangkapan layar suatu laman web dalam mode headless:

`firefox --headless --screenshot {{jalan/menuju/berkas_luaran.png}} {{https://example.com/}}`

- Gunakan profil peramban tertentu untuk memungkinkan Firefox menjalankan berbagai instansi peramban terpisah secara sekaligus:

`firefox --profile {{jalan/menuju/direktori}} {{https://example.com/}}`

- Setel Firefox sebagai peramban bawaan pilihan pada pengaturan sistem operasi:

`firefox --setDefaultBrowser`
