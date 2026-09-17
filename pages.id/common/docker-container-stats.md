# docker container stats

> Siarkan statistik penggunaan sumber daya kontainer.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/stats/>.

- Siarkan statistik untuk seluruh kontainer berjalan:

`docker {{[stats|container stats]}}`

- Siatkan statistik untuk satu atau beberapa kontainer tertentu:

`docker {{[stats|container stats]}} {{kontainer1 kontainer2 ...}}`

- Ubah format kolom luaran untuk menampilkan persentase penggunaan CPU oleh kontainer:

`docker {{[stats|container stats]}} --format "{{.Name}}:\t{{.CPUPerc}}"`

- Siarkan statistik untuk semu[a] kontainer (baik yang dijalankan atau dihentikan):

`docker {{[stats|container stats]}} {{[-a|--all]}}`

- Jangan siarkan namun tampilkan statistik penggunaan saat ini:

`docker {{[stats|container stats]}} --no-stream`
