# act

> Jalankan GitHub Actions secara lokal melalui Docker.
> Informasi lebih lanjut: <https://github.com/nektos/act>.

- Tampilkan daftar actions (tugas dalam GitHub Actions) yang tersedia:

`act -l`

- Jalankan tugas dengan event default:

`act`

- Jalankan event pemicu tugas tertentu:

`act {{jenis_event}}`

- Jalankan tugas/[a]ction tertentu:

`act -a {{action_id}}`

- Tampilkan tugas-tugas yang akan dijalankan ta[n]pa mengeksekusikannya (dry-run):

`act -n`

- Tampilkan log tingkat [v]erbose:

`act -v`

- Jalankan [W]orkflow tertentu:

`act push -W {{jalam/menuju/workflow}}`
