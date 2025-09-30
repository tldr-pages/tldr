# docker ps

> Tampilkan daftar kontainer Docker.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Tampilkan kontainer Docker yang sedang berjalan saat ini:

`docker ps`

- Tampilkan semua kontainer Docker (yang berjalan dan yang berhenti):

`docker ps {{[-a|--all]}}`

- Tampilkan kontainer yang dibuat terakhir (termasuk semua status):

`docker ps {{[-l|--latest]}}`

- Pilah kontainer yang mengandung substring dalam namanya:

`docker ps {{[-f|--filter]}} "name={{nama}}"`

- Pilah kontainer yang memiliki gambar yang sama sebagai leluhur:

`docker ps {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Pilah kontainer berdasarkan kode status keluar (exit status code):

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{kode}}"`

- Pilah kontainer berdasarkan status (created, running, removing, paused, exited, dan dead):

`docker ps {{[-f|--filter]}} "status={{status}}"`

- Pilah kontainer yang mengaitkan suatu volume tertentu atau memiliki volume yang terpasang pada jalur tertentu:

`docker ps {{[-f|--filter]}} "volume={{jalan/menuju/direktori}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
