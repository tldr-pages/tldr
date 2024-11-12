# git credential

> Terima dan simpan kredensial pengguna.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-credential>.

- Tampilkan informasi suatu kredensial, termasuk username dan kata sandi dari berkas-berkas konfigurasi:

`echo "{{url=http://example.com}}" | git credential fill`

- Kirim informasi kredensial menuju seluruh piranti pembantu (credential helper) yang disetel untuk disimpan dan digunakan pada lain waktu:

`echo "{{url=http://example.com}}" | git credential approve`

- Hapus suatu informasi kredensial dari penyimpanan seluruh piranti pembantu:

`echo "{{url=http://example.com}}" | git credential reject`
