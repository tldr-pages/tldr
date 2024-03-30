# git cherry

> Cari komit yang belum dimasukkan kepada hulu (upstream).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-cherry>.

- Lihat daftar komit (beserta pesannya) dengan komit-komit serupa pada hulu (upstream):

`git cherry -v`

- Gunakan sumber hulu dan cabang topik yang lain:

`git cherry {{origin}} {{topik}}`

- Tampilkan hanya komit yang muncul hingga komit ini:

`git cherry {{origin}} {{topic}} {{hingga_komit_ini}}`
