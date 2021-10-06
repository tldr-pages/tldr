# docker ps

> Menampilkan container Docker yang sedang berjalan.
> Informasi lebih lanjut: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Menampilkan semua container docker yang sedang berjalan: 

`docker ps`

- Menampilkan semua container docker (yang berjalan dan dihentikan):

`docker ps --all`

- Menampilkan container terbaru yang dibuat (termasuk statusnya):

`docker ps --latest`

- Menyaring container dengan substring pada namanya:

`docker ps --filter="name={{name}}"`

- Menampilkan container dengan image yang sama sebagai pendahulunya (ancestor):

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Menampilkan container berdasarkan status exit:

`docker ps --all --filter="exited={{code}}"`

- Menampilkan container berdasarkan status (created, running, removing, paused, exited dan dead):

`docker ps --filter="status={{status}}"`

- Menampilkan container yang melakukan mount suatu volume atau memiliki mount volume pada suatudirektori:

`docker ps --filter="volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
