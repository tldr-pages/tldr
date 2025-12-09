# git bug

> Manajer laporan masalah/bug yang menggunakan penyimpanan git, sehingga tidak memengaruhi susunan berkas dalam direktori proyek Anda.
> Anda dapat memasukkan laporan melalui sumber/hulu jauh (remote) yang sama untuk berinteraksi dengan laporan dan pengguna lainnya seperti mengatur komit dan cabang.
> Informasi lebih lanjut: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

- Buat identitas/pengguna baru:

`git bug user create`

- Buat laporan masalah/bug baru:

`git bug add`

- Kumpulkan laporan-laporan baru menuju sumber/hulu jarak jauh:

`git bug push`

- Dapatkan pembaruan atas daftar masalah dari sumber/hulu jarak jauh:

`git bug pull`

- Lihat daftar masalah/bug yang sebelumnya telah dilaporkan:

`git bug ls`

- Saring (filter) dan urutkan (sort) laporan menggunakan kata kunci permintaan tertentu:

`git bug ls "{{status}}:{{open}} {{sort}}:{{edit}}"`

- Cari laporan menurut kata kunci teks:

`git bug ls "{{kata_kunci}}" baz`
