# git clone

> Gandakan repositori dari lokasi luar/remote menuju lokal.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-clone>.

- Gandakan repositori yang ada ke direktori tertentu:

`git clone {{lokasi_repositori_remote}} {{jalan/menuju/direktori}}`

- Gandakan repositori yang ada dan submodulnya:

`git clone --recursive {{lokasi_repositori_remote}}`

- Gandakan hanya direktori `.git` pada repositori saat ini:

`git clone --no-checkout {{lokasi_repositori_remote}}`

- Gandakan repositori lokal:

`git clone --local {{jalan/menuju/repositori/lokal}}`

- Gandakan dengan senyap:

`git clone --quiet {{lokasi_repositori_remote}}`

- Gandakan repositori yang sudah ada dengan hanya mengambil 10 komit paling baru pada branch bawaan (berguna untuk menghemat waktu):

`git clone --depth {{10}} {{lokasi_repositori_remote}}`

- Gandakan repositori yang sudah ada dengan hanya mengambil dari cabang tertentu:

`git clone --branch {{name}} --single-branch {{lokasi_repositori_remote}}`

- Gandakan repositori yang sudah ada menggunakan perintah SSH tertentu:

`git clone --config core.sshCommand="{{ssh -i jalan/menuju/kunci_ssh_privat}}" {{lokasi_repositori_remote}}`
