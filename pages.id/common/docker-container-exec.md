# docker container exec

> Jalankan sebuah perintah dalam suatu kontainer Docker yang sedang berjalan.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Masuk ke dalam sebuah sesi shell interaktif dalam suatu kontainer yang sedang berjalan:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{nama_kontainer}} {{/bin/bash}}`

- Jalankan sebuah perintah dalam latar belakang (mode lepas / detached) dalam suatu kontainer berjalan:

`docker {{[exec|container exec]}} {{[-d|--detach]}} {{nama_kontainer}} {{perintah}}`

- Tentukan alamat direktori kerja yang menjadi pangkal untuk proses eksekusi sebuah perintah:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{jalan/menuju/direktori}} {{nama_kontainer}} {{perintah}}`

- Jalankan sebuah perintah dalam latar belakang dalam kontainer berjalan namun tetap buka saluran `stdin`:

`docker {{[exec|container exec]}} {{[-i|--interactive]}} {{[-d|--detach]}} {{nama_kontainer}} {{perintah}}`

- Tentukan suatu variabel lingkungan untuk suatu sesi shell Bash:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-e|--env]}} {{nama_variabel}}={{nilai}} {{nama_kontainer}} {{/bin/bash}}`

- Jalankan suatu perintah atas nama suatu pengguna dalam kontainer:

`docker {{[exec|container exec]}} {{[-u|--user]}} {{pengguna}} {{nama_kontainer}} {{perintah}}`
