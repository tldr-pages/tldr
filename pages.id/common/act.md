# act

> Jalankan GitHub Actions secara lokal melalui Docker.
> Informasi lebih lanjut: <https://manned.org/act>.

- Tampilkan daftar actions (tugas dalam GitHub Actions) yang tersedia:

`act -l`

- Jalankan tugas dengan event default:

`act`

- Jalankan event pemicu tugas tertentu:

`act {{jenis_event}}`

- Jalankan tugas/[j]ob tertentu:

`act -j {{job_id}}`

- Tampilkan tugas-tugas yang akan dijalankan ta[n]pa mengeksekusikannya (dry-run):

`act -n`

- Tampilkan log tingkat [v]erbose:

`act -v`

- Jalankan [W]orkflow tertentu:

`act push -W {{jalan/menuju/workflow}}`
