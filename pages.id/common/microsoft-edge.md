# microsoft-edge

> Aplikasi peramban web (web browser) dari Microsoft yang dibangun berdasarkan peramban Chromium yang dikembangkan oleh Google.
> Perintah ini tersedia sebagai `msedge` dalam perangkat Windows.
> Catatan: Anda mungkin dapat menggunakan argumen perintah `chromium` lainnya untuk dapat mengatur jalannya Microsoft Edge.
> Informasi lebih lanjut: <https://microsoft.com/edge>.

- Buka suatu URL atau berkas:

`microsoft-edge {{https://example.com|jalan/menuju/berkas.html}}`

- Buka dalam mode peramban privat (InPrivate):

`microsoft-edge --inprivate {{example.com}}`

- Buka dalam jendela aplikasi baru:

`microsoft-edge --new-window {{example.com}}`

- Buka dalam mode aplikasi web (tanpa bilah toolbar, URL bar, tombol navigasi, dsb.):

`microsoft-edge --app={{https://example.com}}`

- Hubungkan peramban dengan suatu peladen proksi:

`microsoft-edge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Buka dengan direktori profil pengguna tertentu:

`microsoft-edge --user-data-dir={{jalan/menuju/direktori}}`

- Buka dengan menonaktifkan validasi CORS (berguna untuk menguji akses suatu API):

`microsoft-edge --user-data-dir={{jalan/menuju/direktori}} --disable-web-security`

- Selalu buka jendela alat DevTools (pembantu pengembang web) setiap kali membuka tab baru:

`microsoft-edge --auto-open-devtools-for-tabs`
