# apptainer overlay

> Kelola image overlay EXT3 yang dapat ditulisi untuk kontainer Apptainer.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_overlay.html>.

- Tambahkan overlay yang dapat ditulisi ke image SIF yang sudah ada:

`apptainer overlay create {{[-s|--size]}} {{size}} {{path/ke/image.sif}}`

- Buat image overlay EXT3 mandiri yang dapat ditulisi:

`apptainer overlay create {{[-s|--size]}} {{size}} {{path/ke/overlay.img}}`

- Buat image overlay sparse:

`apptainer overlay create {{[-s|--size]}} {{size}} {{[-S|--sparse]}} {{path/ke/overlay.img}}`

- Buat overlay untuk digunakan dengan fakeroot:

`apptainer overlay create {{[-f|--fakeroot]}} {{[-s|--size]}} {{size}} {{path/ke/overlay.img}}`

- Buat overlay dengan direktori tertentu di dalam layout:

`apptainer overlay create --create-dir {{path/ke/direktori}} {{path/ke/overlay.img}}`

- Tampilkan bantuan:

`apptainer overlay {{[-h|--help]}}`
