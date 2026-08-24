# docker container update

> Mutakhirkan konfigurasi sistem dalam kumpulan kontainer Docker.
> Catatan: Perintah ini tidak mendukung kumpulan kontainer Windows.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/update/>.

- Perbarui kebijakan pemuatan ulang (restart policy) saat suatu kontainer berhenti:

`docker {{[update|container update]}} --restart {{always|no|on-failure|unless-stopped}} {{nama_kontainer}}`

- Perbarui kebijakan untuk mencoba memuat ulang hingga tiga kali kesempatan untuk suatu kontainer yang berhenti dengan kode exit non-nihil:

`docker {{[update|container update]}} --restart on-failure:3 {{nama_kontainer}}`

- Perbarui jumlah CPU yang dialokasikan untuk suatu kontainer:

`docker {{[update|container update]}} --cpus {{jumlah_cpu}} {{nama_kontainer}}`

- Perbarui batas memori dalam satuan [M]egabita untuk suatu kontainer:

`docker {{[update|container update]}} {{[-m|--memory]}} {{batas}}M {{nama_kontainer}}`

- Perbarui batas maksimum nomor induk proses (Process ID) dalam suatu kontainer (gunakan `-1` untuk tak terbatas):

`docker {{[update|container update]}} --pids-limit {{batas}} {{nama_kontainer}}`

- Perbarui jumlah memori swap dalam satuan [M]egabita untuk suatu kontainer (gunakan `-1` untuk tak terbatas):

`docker {{[update|container update]}} --memory-swap {{batas}}M {{nama_kontainer}}`
