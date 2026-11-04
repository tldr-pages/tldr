# docker login

> Masuk menuju suatu registry Docker menggunakan akun terdaftar.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/login/>.

- Masuk ke dalam suatu registry secara interaktif:

`docker login`

- Masuk ke dalam suatu registry menggunakan nama pengguna tertentu (kata sandi akan kemudian ditanyakan kepada pengguna):

`docker login {{[-u|--username]}} {{nama_pengguna}}`

- Masuk ke dalam suatu registry menggunakan nama dan kata sandi pengguna:

`docker login {{[-u|--username]}} {{nama_pengguna}} {{[-p|--password]}} {{kata_sandi}} {{peladen}}`

- Masuk ke dalam suatu registry menggunakan kata sandi dari `stdin`:

`echo "{{kata_sandi}}" | docker login {{[-u|--username]}} {{nama_pengguna}} --password-stdin`
