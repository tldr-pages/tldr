# docker compose

> Jalankan dan kelola aplikasi Docker dengan beberapa kontainer.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/compose/>.

- Tampilkan semua kontainer yang sedang berjalan:

`docker compose ps`

- Buat dan nyalakan semua kontainer di latar belakang menggunakan file docker-compose.yml dari direktori saat ini:

`docker compose up {{[-d|--detach]}}`

- Nyalakan semua kontainer, dan bangun ulang jika diperlukan:

`docker compose up --build`

- Nyalakan semua kontainer dengan menentukan nama proyek dan menggunakan file compose alternatif:

`docker compose {{[-p|--project-name]}} {{nama_proyek}} {{[-f|--file]}} {{jalan/menuju/file}} up`

- Hentikan semua kontainer yang sedang berjalan:

`docker compose stop`

- Hentikan dan menghapus semua kontainer, jaringan, image, dan volume:

`docker compose down --rmi all {{[-v|--volumes]}}`

- Ikuti log untuk semua kontainer:

`docker compose logs {{[-f|--follow]}}`

- Ikuti log untuk kontainer tertentu:

`docker compose logs {{[-f|--follow]}} {{container_name}}`
