# wsl

> Atur modul Subsistem Windows untuk Linux (WSL).
> Informasi lebih lanjut: <https://learn.microsoft.com/windows/wsl/reference>.

- Jalankan suatu sesi syel Linux (di dalam distribusi default):

`wsl {{perintah_syel}}`

- Jalankan suatu perintah Linux tanpa menggunakan suatu syel:

`wsl {{[-e|--exec]}} {{perintah}} {{kumpulan_argumen_perintah}}`

- Gunakan suatu distribusi (distro) tertentu:

`wsl {{[-d|--distribution]}} {{distribusi}} {{perintah_syel}}`

- Tampilkan daftar distribusi yang tersedia:

`wsl {{[-l|--list]}}`

- Ekspor suatu distribusi ke dalam berkas `.tar`:

`wsl --export {{distribusi}} {{jalan\menuju\berkas_distro.tar}}`

- Impor suatu distribusi dari berkas `tar`:

`wsl --import {{distribusi}} {{jalan\menuju\lokasi_pemasangan}} {{jalan/menuju/berkas_distro.tar}}`

- Ubah versi wsl yang digunakan untuk suatu distribusi:

`wsl --set-version {{distribusi}} {{versi}}`

- Matikan Subsistem Windows untuk Linux:

`wsl --shutdown`
