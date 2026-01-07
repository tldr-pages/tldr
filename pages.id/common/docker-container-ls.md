# docker container ls

> Tampilkan daftar kontainer Docker.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Tampilkan kontainer Docker yang sedang berjalan saat ini:

`docker {{[ps|container ls]}}`

- Tampilkan semua kontainer Docker (yang berjalan dan yang berhenti):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Tampilkan kontainer yang dibuat terakhir (termasuk semua status):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Pilah kontainer yang mengandung substring dalam namanya:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{nama}}"`

- Pilah kontainer yang memiliki gambar yang sama sebagai leluhur:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Pilah kontainer berdasarkan kode status keluar (exit status code):

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{kode}}"`

- Pilah kontainer berdasarkan status (created, running, removing, paused, exited, dan dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{status}}"`

- Pilah kontainer yang mengaitkan suatu volume tertentu atau memiliki volume yang terpasang pada jalur tertentu:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{jalan/menuju/direktori}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
