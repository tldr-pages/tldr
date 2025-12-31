# ssh-add

> Mengelola kunci SSH yang dimuat di dalam `ssh-agent`.
> Pastikan `ssh-agent` sudah berjalan agar kunci dapat dimuat ke dalamnya.
> Informasi lebih lanjut: <https://man.openbsd.org/ssh-add>.

- Tambahkan kunci SSH default di `~/.ssh` ke ssh-agent:

`ssh-add`

- Tambahkan kunci spesifik ke ssh-agent:

`ssh-add {{lokasi/ke/kunci_privat}}`

- Tampilkan sidik jari (fingerprint) dari kunci yang sedang dimuat:

`ssh-add -l`

- Hapus sebuah kunci dari ssh-agent:

`ssh-add -d {{lokasi/ke/kunci_privat}}`

- Hapus semua kunci yang sedang dimuat dari ssh-agent:

`ssh-add -D`

- Tambahkan kunci ke ssh-agent dan keychain:

`ssh-add -K {{lokasi/ke/kunci_privat}}`
