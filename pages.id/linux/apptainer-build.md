# apptainer build

> Buat image container Apptainer.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_build.html>.

- Buat container dari sebuah file definisi:

`apptainer build {{path/ke/image.sif}} {{path/ke/definition.def}}`

- Buat container dari Docker Hub:

`apptainer build {{path/ke/image.sif}} docker://{{image}}:{{tag}}`

- Buat container dari Container Library:

`apptainer build {{path/ke/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Buat direktori sandbox yang dapat ditulis alih-alih file image:

`apptainer build {{[-s|--sandbox]}} {{path/ke/direktori}} docker://{{image}}:{{tag}}`

- Buat container tanpa menggunakan cache:

`apptainer build --disable-cache {{path/ke/image.sif}} docker://{{image}}:{{tag}}`

- Paksa timpa file image yang sudah ada:

`apptainer build {{[-F|--force]}} {{path/ke/image.sif}} {{path/ke/definition.def}}`

- Buat menggunakan fakeroot untuk build unprivileged:

`apptainer build {{[-f|--fakeroot]}} {{path/ke/image.sif}} {{path/ke/definition.def}}`

- Tampilkan bantuan:

`apptainer build {{[-h|--help]}}`
