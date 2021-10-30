# git clone

> Mengkloning repositori yang ada.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-clone>.

- Mengkloning repositori yang ada:

`git clone {{lokasi_repositori_remote}}`

- Mengkloning reposiori yang ada dan submodulenya:

`git clone --recursive {{lokasi_repositori_remote}}`

- Mengkloning repositori lokal:

`git clone -l {{alamat/ke/repository/lokal}}`

- Mengkloning dengan senyap:

`git clone -q {{lokasi_repositori_remote}}`

- Mengkloning repositori yang sudah ada dengan hanya mengambil 10 komit paling baru pada branch default (berguna untuk menghemat waktu):

`git clone --depth {{10}} {{lokasi_repositori_remote}}`
