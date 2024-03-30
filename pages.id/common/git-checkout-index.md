# git checkout-index

> Salin file dari indeks menuju direktori kerja saat ini.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-checkout-index>.

- Pulihkan berkas-berkas yang terhapus sejak komit terakhir:

`git checkout-index --all`

- Pulihkan berkas-berkas yang terhapus atau termodifikasi sejak komit terakhir:

`git checkout-index --all --force`

- Pulihkan berkas-berkas yang diubah sejak komit terakhir, mengabaikan berkas-berkas yang telah dihapus sebelumnya:

`git checkout-index --all --force --no-create`

- Ekspor sebuah salinan pohon (tree) pada komit terakhir kepada suatu direktori (nama direktori pada `--prefix` perlu diakhiri dengan garis miring):

`git checkout-index --all --force --prefix={{jalan/menuju/direktori_ekspor/}}`
