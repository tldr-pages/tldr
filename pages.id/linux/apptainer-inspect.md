# apptainer inspect

> Tampilkan metadata dari image kontainer Apptainer.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_inspect.html>.

- Tampilkan label dari sebuah image (bawaan):

`apptainer inspect {{path/ke/image.sif}}`

- Tampilkan file definisi yang digunakan untuk membangun image:

`apptainer inspect {{[-d|--deffile]}} {{path/ke/image.sif}}`

- Tampilkan runscript untuk suatu image:

`apptainer inspect {{[-r|--runscript]}} {{path/ke/image.sif}}`

- Tampilkan variabel environment dari suatu image:

`apptainer inspect {{[-e|--environment]}} {{path/ke/image.sif}}`

- Tampilkan daftar semua aplikasi di dalam kontainer:

`apptainer inspect --list-apps {{path/ke/image.sif}}`

- Tampilkan semua data yang tersedia dalam format JSON:

`apptainer inspect --all {{path/ke/image.sif}}`

- Tampilkan bantuan:

`apptainer inspect {{[-h|--help]}}`
