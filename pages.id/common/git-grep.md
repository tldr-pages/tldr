# git grep

> Cari kumpulan teks atau string dalam berkas-berkas yang diawasi dalam suatu repositori.
> Menerima banyak jenis flag atau argumen khusus dari program reguler `grep`.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-grep>.

- Cari untuk suatu string dalam berkas-berkas dalam `HEAD` saat ini:

`git grep "{{pola_pencarian_string}}"`

- Cari untuk suatu string dalam berkas-berkas yang memenuhi suatu pola glob nama berkas dalam `HEAD` saat ini:

`git grep "{{pola_pencarian_string}}" -- "{{*.ext}}"`

- Cari suatu string termasuk dalam kumpulan submodul Git:

`git grep --recurse-submodules "{{pola_pencarian_string}}"`

- Cari suatu string dalam titik riwayat perubahan tertentu:

`git grep "{{pola_pencarian_string}}" {{HEAD~2}}`

- Cari suatu string dalam seluruh cabang dan seluruh riwayat perubahan:

`git grep "{{pola_pencarian_string}}" $(git rev-list --all)`
