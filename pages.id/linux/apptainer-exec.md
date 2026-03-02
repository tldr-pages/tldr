# apptainer exec

> Jalankan perintah di dalam container Apptainer.
> Lihat juga: `apptainer run`, `apptainer shell`.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_exec.html>.

- Jalankan perintah di dalam container:

`apptainer exec {{path/ke/image.sif}} {{command}}`

- Jalankan perintah beserta argumen:

`apptainer exec {{path/ke/image.sif}} {{command}} {{arg1 arg2 ...}}`

- Jalankan perintah dengan bind mount dari host ke container:

`apptainer exec {{[-B|--bind]}} {{path/ke/sumber}}:{{path/ke/tujuan}} {{path/ke/image.sif}} {{command}}`

- Jalankan perintah dengan variabel environment:

`apptainer exec --env {{variable}}={{value}} {{path/ke/image.sif}} {{command}}`

- Jalankan perintah dalam mode terisolasi penuh (filesystem terisolasi, PID, IPC, dan environment yang bersih):

`apptainer exec {{[-C|--containall]}} {{path/ke/image.sif}} {{command}}`

- Jalankan perintah dengan overlay filesystem sementara yang bisa ditulis:

`apptainer exec --writable-tmpfs {{path/ke/image.sif}} {{command}}`

- Jalankan perintah dengan dukungan GPU NVIDIA:

`apptainer exec --nv {{path/ke/image.sif}} {{command}}`

- Tampilkan bantuan:

`apptainer exec {{[-h|--help]}}`
