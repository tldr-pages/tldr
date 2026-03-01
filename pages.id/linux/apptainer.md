# apptainer

> Kelola container untuk HPC dan komputasi ilmiah.
> Beberapa subperintah seperti `build`, `pull`, dan `push` memiliki dokumentasi penggunaan tersendiri.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli.html>.

- Unduh container dari Docker Hub:

`apptainer pull {{path/ke/image.sif}} docker://{{image}}:{{tag}}`

- Unduh container dari Container Library:

`apptainer pull {{path/ke/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Buat container dari file definisi:

`apptainer build {{path/ke/image.sif}} {{path/ke/definisi.def}}`

- Mulai shell interaktif di dalam container:

`apptainer shell {{path/ke/image.sif}}`

- Jalankan perintah di dalam container:

`apptainer exec {{path/ke/image.sif}} {{command}}`

- Jalankan runscript setelan standar (default) dari sebuah container:

`apptainer run {{path/ke/image.sif}}`

- Periksa metadata dari sebuah container:

`apptainer inspect {{path/ke/image.sif}}`

- Tampilkan bantuan:

`apptainer {{[-h|--help]}}`
