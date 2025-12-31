# xattr

> Utilitas untuk bekerja dengan atribut sistem berkas yang diperluas.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/xattr.1.html>.

- Tampilkan daftar atribut kunci:nilai yang diperluas untuk berkas tertentu:

`xattr -l {{berkas}}`

- Tulis atribut untuk suatu berkas:

`xattr -w {{kunci_atribut}} {{nilai_atribut}} {{berkas}}`

- Hapus atribut dari suatu berkas:

`xattr -d {{com.apple.quarantine}} {{berkas}}`

- Hapus semua atribut yang diperluas dari suatu berkas:

`xattr -c {{berkas}}`

- Hapus atribut secara rekursif dalam direktori tertentu:

`xattr -rd {{kunci_atribut}} {{direktori}}`
