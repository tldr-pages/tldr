# git clone

> Klon repositori yang ada.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-clone>.

- Klon repositori yang ada ke direktori tertentu:

`git clone {{lokasi_repositori_remote}} {{jalan/menuju/direktori}}`

- Klon repositori yang ada dan submodulnya:

`git clone --recursive {{lokasi_repositori_remote}}`

- Klon repositori lokal:

`git clone --local {{jalan/menuju/repositori/lokal}}`

- Klon dengan senyap:

`git clone --quiet {{lokasi_repositori_remote}}`

- Klon repositori yang sudah ada dengan hanya mengambil 10 komit paling baru pada branch bawaan (berguna untuk menghemat waktu):

`git clone --depth {{10}} {{lokasi_repositori_remote}}`

- Klon repositori yang sudah ada dengan hanya mengambil dari cabang tertentu:

`git clone --branch {{name}} --single-branch {{lokasi_repositori_remote}}`

- Klon repositori yang sudah ada menggunakan perintah SSH tertentu:

`git clone --config core.sshCommand="{{ssh -i jalan/menuju/kunci_ssh_pribadi}}" {{lokasi_repositori_remote}}`
