# apptainer inspect

> Tampilkan metadata dari image kontainer Apptainer.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_inspect.html>.

- Tampilkan label dari sebuah image (bawaan):

`apptainer inspect {{jalan/menuju/image.sif}}`

- Tampilkan file definisi yang digunakan untuk membangun image:

`apptainer inspect {{[-d|--deffile]}} {{jalan/menuju/image.sif}}`

- Tampilkan runscript untuk suatu image:

`apptainer inspect {{[-r|--runscript]}} {{jalan/menuju/image.sif}}`

- Tampilkan variabel environment dari suatu image:

`apptainer inspect {{[-e|--environment]}} {{jalan/menuju/image.sif}}`

- Tampilkan daftar semua aplikasi di dalam kontainer:

`apptainer inspect --list-apps {{jalan/menuju/image.sif}}`

- Tampilkan semua data yang tersedia dalam format JSON:

`apptainer inspect --all {{jalan/menuju/image.sif}}`

- Tampilkan bantuan:

`apptainer inspect {{[-h|--help]}}`
