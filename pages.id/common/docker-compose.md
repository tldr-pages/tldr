# docker compose

> Jalankan dan kelola aplikasi Docker dengan beberapa kontainer.
> Informasi lebih lanjut: <https://docs.docker.com/compose/reference/>.

- Tampilkan semua kontainer yang sedang berjalan:

`docker compose ps`

- Buat dan nyalakan semua kontainer di latar belakang menggunakan file docker-compose.yml dari direktori saat ini:

`docker compose up --detach`

- Nyalakan semua kontainer, dan bangun ulang jika diperlukan:

`docker compose up --build`

- Nyalakan semua kontainer dengan menentukan nama proyek dan menggunakan file compose alternatif:

`docker compose -p {{nama_proyek}} --file {{jalan/menuju/file}} up`

- Hentikan semua kontainer yang sedang berjalan:

`docker compose stop`

- Hentikan dan menghapus semua kontainer, jaringan, image, dan volume:

`docker compose down --rmi all --volumes`

- Ikuti log untuk semua kontainer:

`docker compose logs --follow`

- Ikuti log untuk kontainer tertentu:

`docker compose logs --follow {{container_name}}`
