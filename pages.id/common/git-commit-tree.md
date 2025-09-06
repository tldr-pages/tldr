# git commit-tree

> Alat untuk membuat objek komit secara tingkat rendah (low-level).
> Lihat juga: `git commit`.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-commit-tree>.

- Buat objek komit baru dengan pesan tertentu:

`git commit-tree {{tree}} -m "{{pesan}}"`

- Buat objek komit dengan pesan yang disimpan dalam suatu berkas (gunakan `-` untuk membaca dari `stdin`):

`git commit-tree {{tree}} -F {{jalan/menuju/berkas}}`

- Buat sebuah objek komit yang ditandatangani oleh kunci enkripsi GPG:

`git commit-tree {{tree}} -m "{{pesan}}" --gpg-sign`

- Buat sebuah objek komit dengan komit induk tertentu:

`git commit-tree {{tree}} -m "{{message}}" -p {{kode_hash_sha_atas_komit_induk}}`
