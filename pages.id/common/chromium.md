# chromium

> Aplikasi peramban web (web browser) bersumber terbuka yang terutama dikembangkan dan dikelola oleh Google.
> Catatan: Anda mungkin perlu menggantikan perintah `chromium` dengan peramban tujuan Anda, seperti `brave`, `google-chrome`, `opera`, atau `vivaldi`.
> Informasi lebih lanjut: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Buka suatu URL atau berkas:

`chromium {{https://example.com|jalan/menuju/berkas.html}}`

- Buka dalam mode peramban privat (incognito):

`chromium --incognito {{example.com}}`

- Buka dalam jendela aplikasi baru:

`chromium --new-window {{example.com}}`

- Buka dalam mode aplikasi web (tanpa bilah toolbar, URL bar, tombol navigasi, dsb.):

`chromium --app={{https://example.com}}`

- Hubungkan peramban dengan suatu peladen proksi:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Buka dengan direktori profil pengguna tertentu:

`chromium --user-data-dir={{jalan/menuju/direktori}}`

- Buka dengan menonaktifkan validasi CORS (berguna untuk menguji akses suatu API):

`chromium --user-data-dir={{jalan/menuju/direktori}} --disable-web-security`

- Selalu buka jendela alat DevTools (pembantu pengembang web) setiap kali membuka tab baru:

`chromium --auto-open-devtools-for-tabs`
