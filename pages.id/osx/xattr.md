# xattr

> Utilitas untuk bekerja dengan atribut sistem berkas yang diperluas.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/xattr.1.html>.

- Tampilkan daftar atribut kunci:nilai yang diperluas untuk berkas tertentu:

`xattr -l {{berkas}}`

- Menulis atribut untuk berkas tertentu:

`xattr -w {{kunci_atribut}} {{nilai_atribut}} {{berkas}}`

- Menghapus atribut dari berkas tertentu:

`xattr -d {{com.apple.quarantine}} {{berkas}}`

- Menghapus semua atribut yang diperluas dari berkas tertentu:

`xattr -c {{berkas}}`

- Menghapus atribut secara rekursif dalam direktori tertentu:

`xattr -rd {{kunci_atribut}} {{direktori}}`
