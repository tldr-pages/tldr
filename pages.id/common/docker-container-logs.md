# docker container logs

> Cetak isi log sistem dalam kumpulan kontainer.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Cetak isi log dalam suatu kontainer:

`docker {{[logs|container logs]}} {{nama_kontainer}}`

- Cetak isi log dan tetap ikuti untuk menerima pesan log baru:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{nama_kontainer}}`

- Hanya cetak 5 baris log terakhir:

`docker {{[logs|container logs]}} {{nama_kontainer}} {{[-n|--tail]}} 5`

- Cetak isi log beserta waktu di mana setiap pesan muncul:

`docker {{[logs|container logs]}} {{[-t|--timestamps]}} {{nama_kontainer}}`

- Cetak isi log yang muncul sejak waktu lampau yang ditentukan (misalnya 23m, 10s, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{nama_kontainer}} --until {{waktu}}`
