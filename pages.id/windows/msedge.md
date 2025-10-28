# msedge

> Aplikasi peramban web (web browser) dari Microsoft yang dibangun berdasarkan peramban Chromium yang dikembangkan oleh Google.
> Perintah ini tersedia sebagai `microsoft-edge` dalam perangkat selain Windows.
> Catatan: Anda mungkin dapat menggunakan argumen perintah `chromium` lainnya untuk dapat mengatur jalannya Microsoft Edge.
> Informasi lebih lanjut: <https://microsoft.com/edge>.

- Buka suatu URL atau berkas:

`msedge {{https://example.com|jalan\menuju\berkas.html}}`

- Buka dalam mode peramban privat (InPrivate):

`msedge --inprivate {{example.com}}`

- Buka dalam jendela aplikasi baru:

`msedge --new-window {{example.com}}`

- Buka dalam mode aplikasi web (tanpa bilah toolbar, URL bar, tombol navigasi, dsb.):

`msedge --app={{https://example.com}}`

- Hubungkan peramban dengan suatu peladen proksi:

`msedge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Buka dengan direktori profil pengguna tertentu:

`msedge --user-data-dir={{jalan\menuju\direktori}}`

- Buka dengan menonaktifkan validasi CORS (berguna untuk menguji akses suatu API):

`msedge --user-data-dir={{jalan\menuju\direktori}} --disable-web-security`

- Selalu buka jendela alat DevTools (pembantu pengembang web) setiap kali membuka tab baru:

`msedge --auto-open-devtools-for-tabs`
