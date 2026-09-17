# aa-update-browser

> Perbarui profil browser AppArmor agar menggunakan abstraksi yang didukung.
> Bagian dari paket AppArmor.
> Informasi lebih lanjut: <https://manned.org/aa-update-browser>.

- Tampilkan daftar profil abstraksi browser yang tersedia:

`sudo aa-update-browser -l`

- Tampilkan perubahan apa yang akan dibuat pada sebuah profil tanpa menerapkannya (dry-run):

`sudo aa-update-browser -d {{path/ke/profil}}`

- Perbarui profil dengan abstraksi tertentu:

`sudo aa-update-browser -u {{abstraction1,abstraction2,...}} {{path/ke/profil}}`

- Hapus semua abstraksi dari sebuah profil:

`sudo aa-update-browser -u '' {{path/ke/profil}}`

- Tampilkan bantuan:

`aa-update-browser -h`
