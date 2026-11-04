# batch

> Tunda dan jalankan kumpulan perintah sesaat beban kerja sistem komputer mencukupi.
> Hasil kerja akan dikirimkan menuju kotak surel pengguna.
> Lihat juga: `at`, `atq`, `atrm`, `mail`.
> Informasi lebih lanjut: <https://manned.org/batch>.

- Jalankan kumpulan perintah dari `stdin` (tekan `<Ctrl d>` untuk mengakhiri):

`batch`

- Jalankan satu perintah saja dari `stdin`:

`echo "{{./buat_cadangan_db.sh}}" | batch`
