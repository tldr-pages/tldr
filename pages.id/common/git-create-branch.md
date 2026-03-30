# git create-branch

> Buat suatu cabang (branch) baru dalam suatu repositori Git.
> Bagian dari `git-extras`.
> Informasi lebih lanjut: <https://manned.org/git-create-branch>.

- Buat suatu cabang baru pada repositori lokal:

`git create-branch {{nama_cabang}}`

- Buat cabang baru pada repositori lokal dan sumber jarak jauh (remote) origin:

`git create-branch {{[-r|--remote]}} {{nama_cabang}}`

- Buat cabang baru pada repositori lokal dan sumber jarak jauh (remote) upstream (yang dibentuk melalui proses pencangkokan/fork):

`git create-branch {{[-r|--remote]}} upstream {{nama_cabang}}`
