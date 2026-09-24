# apptainer

> Kelola container untuk HPC dan komputasi ilmiah.
> Beberapa subperintah seperti `build`, `pull`, dan `push` memiliki dokumentasi penggunaan tersendiri.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli.html>.

- Unduh container dari Docker Hub:

`apptainer pull {{jalan/menuju/image.sif}} docker://{{image}}:{{tag}}`

- Unduh container dari Container Library:

`apptainer pull {{jalan/menuju/image.sif}} library://{{pengguna/koleksi/container}}:{{tag}}`

- Buat container dari file definisi:

`apptainer build {{jalan/menuju/image.sif}} {{jalan/menuju/definisi.def}}`

- Mulai shell interaktif di dalam container:

`apptainer shell {{jalan/menuju/image.sif}}`

- Jalankan perintah di dalam container:

`apptainer exec {{jalan/menuju/image.sif}} {{perintah}}`

- Jalankan runscript setelan standar (default) dari sebuah container:

`apptainer run {{jalan/menuju/image.sif}}`

- Periksa metadata dari sebuah container:

`apptainer inspect {{jalan/menuju/image.sif}}`

- Tampilkan bantuan:

`apptainer {{[-h|--help]}}`
