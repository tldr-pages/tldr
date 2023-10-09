# docker ps

> Tampilkan daftar kontainer Docker.
> Informasi lebih lanjut: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Tampilkan kontainer Docker yang sedang berjalan saat ini:

`docker ps`

- Tampilkan semua kontainer Docker (yang berjalan dan yang berhenti):

`docker ps --all`

- Tampilkan kontainer yang dibuat terakhir (termasuk semua status):

`docker ps --latest`

- Pilah kontainer yang mengandung substring dalam namanya:

`docker ps --filter="name={{nama}}"`

- Pilah kontainer yang memiliki gambar yang sama sebagai leluhur:

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Pilah kontainer berdasarkan kode status keluar (exit status code):

`docker ps --all --filter="exited={{kode}}"`

- Pilah kontainer berdasarkan status (created, running, removing, paused, exited, dan dead):

`docker ps --filter="status={{status}}"`

- Pilah kontainer yang mengaitkan suatu volume tertentu atau memiliki volume yang terpasang pada jalur tertentu:

`docker ps --filter="volume={{jalan/menuju/direktori}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
