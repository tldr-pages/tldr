# AdGuardHome

> Perangkat lunak untuk memblokir iklan dan upaya pelacakan dalam jaringan internet.
> Informasi lebih lanjut: <https://github.com/AdguardTeam/AdGuardHome>.

- Jalankan AdGuard Home:

`AdGuardHome`

- Jalankan AdGuard Home dengan konfigurasi tertentu:

`AdGuardHome --config {{jalan/menuju/AdGuardHome.yaml}}`

- Tentukan direktori penyimpanan data untuk AdGuard Home:

`AdGuardHome --work-dir {{jalan/menuju/direktori}}`

- Pasang atau bongkar AdGuard Home sebagai layanan/daemon sistem operasi:

`AdGuardHome --service {{install|uninstall}}`

- Jalankan AdGuard Home sebagai layanan/daemon:

`AdGuardHome --service start`

- Muat ulang konfigurasi layanan AdGuard Home:

`AdGuardHome --service reload`

- Matikan atau nyalakan ulang layanan AdGuard Home:

`AdGuardHome --service {{stop|restart}}`
