# apptainer build

> Buat image container Apptainer.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_build.html>.

- Buat container dari sebuah file definisi:

`apptainer build {{jalan/menuju/image.sif}} {{jalan/menuju/definisi.def}}`

- Buat container dari Docker Hub:

`apptainer build {{jalan/menuju/image.sif}} docker://{{image}}:{{tag}}`

- Buat container dari Container Library:

`apptainer build {{jalan/menuju/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Buat direktori sandbox yang dapat ditulis alih-alih file image:

`apptainer build {{[-s|--sandbox]}} {{jalan/menuju/direktori}} docker://{{image}}:{{tag}}`

- Buat container tanpa menggunakan cache:

`apptainer build --disable-cache {{jalan/menuju/image.sif}} docker://{{image}}:{{tag}}`

- Paksa timpa file image yang sudah ada:

`apptainer build {{[-F|--force]}} {{jalan/menuju/image.sif}} {{jalan/menuju/definition.def}}`

- Buat menggunakan fakeroot untuk build unprivileged:

`apptainer build {{[-f|--fakeroot]}} {{jalan/menuju/image.sif}} {{jalan/menuju/definition.def}}`

- Tampilkan bantuan:

`apptainer build {{[-h|--help]}}`
