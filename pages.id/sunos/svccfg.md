# svccfg

> Impor, ekspor, dan modifikasi konfigurasi servis.
> Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validasi berkas konfigurasi:

`svccfg validate {{jalan/menuju/berkas_smf.xml}}`

- Ekspor konfigurasi servis kedalam sebuah berkas:

`svccfg export {{nama_servis}} > {{jalur/ke/berkas_smf.xml}}`

- Impor/perbarui konfigurasi servis dari berkas:

`svccfg import {{jalan/menuju/berkas_smf.xml}}`
