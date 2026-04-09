# docker container

> Atur kumpulan kontainer Docker.
> Informasi lebioh lanjut: <https://docs.docker.com/reference/cli/docker/container/>.

- Tampilkan daftar kontainer Docker yang sedang berjalan:

`docker {{[ps|container ls]}}`

- Jalankan satu atau beberapa kontainer yang dihentikan:

`docker {{[start|container start]}} {{nama_kontainer1}} {{nama_kontainer2}}`

- Matikan satu atau beberapa kontainer:

`docker {{[kill|container kill]}} {{nama_kontainer1}} {{nama_kontainer2}}`

- Hentikan satu atau beberapa kontainer:

`docker {{[stop|container stop]}} {{nama_kontainer1}} {{nama_kontainer2}}`

- Jedakan seluruh proses dalam satu atau beberapa kontainer:

`docker {{[pause|container pause]}} {{nama_kontainer1}} {{nama_kontainer2}}`

- Tampilkan rincian informasi mengenai satu atau beberapa kontainer:

`docker container inspect {{nama_kontainer1}} {{nama_kontainer2}}`

- Arsip suatu sistem penyimpanan pada kontainer ke dalam berkas `.tar`:

`docker {{[export|container export]}} {{nama_kontainer}}`

- Buat suatu citra (image) baru atas perubahan-perubahan yang dilakukan di dalam suatu kontainer:

`docker {{[commit|container commit]}} {{nama_kontainer}}`
