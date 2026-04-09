# docker container run

> Jalankan suatu perintah dalam suatu kontainer Docker baru.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Jalankan perintah dalam suatu kontainer baru dari suatu citra dengan label/tag tertentu:

`docker {{[run|container run]}} {{citra:tag}} {{perintah}}`

- Jalankan perintah dalam suatu kontainer baru secara latar belakang dan tampilkan ID kontainer baru yang dibuat:

`docker {{[run|container run]}} {{[-d|--detach]}} {{citra}} {{perintah}}`

- Jalankan perintah dalam sebuah kontainer sekali pakai dalam mode interaktif dan pseudo-TTY:

`docker {{[run|container run]}} --rm {{[-it|--interactive --tty]}} {{citra}} {{perintah}}`

- Jalankan perintah dalam suatu kontainer dengan meneruskan variabel lingkungan

`docker {{[run|container run]}} {{[-e|--env]}} '{{variabel}}={{nilai}}' {{[-e|--env]}} {{variabel}} {{citra}} {{perintah}}`

- Jalankan perintah dalam suatu kontainer baru dengan memadankan volume penyimpanan:

`docker {{[run|container run]}} {{[-v|--volume]}} /{{jalan/menuju/berkas_atau_direktori_penyimpanan_induk}}:/{{jalan/menuju/berkas_atau_direktori_dalam_kontainer}} {{citra}} {{perintah}}`

- Jalankan perintah dalam suatu kontainer baru dengan daftar port untuk diteruskan/dipublikasikan:

`docker {{[run|container run]}} {{[-p|--publish]}} {{port_perangkat_induk}}:{{port_dalam_kontainer}} {{citra}} {{perintah}}`

- Jalankan perintah dalam suatu kontainer baru dengan menggantikan perintah awal (entrypoint) dalam citra yang dipilih:

`docker {{[run|container run]}} --entrypoint {{perintah}} {{citra}}`

- Jalankan perintah dalam suatu kontainer baru dan hubungkan ke dalam suatu jaringan:

`docker {{[run|container run]}} --network {{network}} {{citra}}`
