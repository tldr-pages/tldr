# docker context

> Pindah antar konteks untuk mengelola beberapa lingkungan pemasangan Docker.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/context/>.

- Buat suatu konteks baru menggunakan titik akses (endpoint) peladen Docker:

`docker context create {{nama_konteks}} --docker "host={{tcp://host-jarak-jauh:2375}}"`

- Buat suatu konteks baru berdasarkan informasi nilai variable lingkungan `$DOCKER_HOST` saat ini:

`docker context create {{nama_konteks}}`

- Pindah menuju konteks lainnya:

`docker context use {{nama_konteks}}`

- Tampilkan daftar nama konteks:

`docker context ls`
