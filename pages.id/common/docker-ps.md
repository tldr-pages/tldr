# docker ps

> Tampilkan daftar kontainer Docker.
> Informasi lebih lanjut: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Tampilkan kontainer Docker yang sedang berjalan saat ini:

`docker ps`

- Menampilkan semua kontainer Docker (yang berjalan dan yang berhenti):

`docker ps --all`

- Menampilkan kontainer yang dibuat terakhir (termasuk semua status):

`docker ps --latest`

- Memilah kontainer yang mengandung substring dalam namanya:

`docker ps --filter="name={{nama}}"`

- Memilah kontainer yang memiliki gambar yang sama sebagai leluhur:

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Memilah kontainer berdasarkan kode status keluar (exit status code):

`docker ps --all --filter="exited={{kode}}"`

- Memilah kontainer berdasarkan status (created, running, removing, paused, exited, dan dead):

`docker ps --filter="status={{status}}"`

- Memilah kontainer yang mengaitkan suatu volume tertentu atau memiliki volume yang terpasang pada jalur tertentu:

`docker ps --filter="volume={{jalan/menuju/direktori}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
