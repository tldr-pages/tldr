# dnf

> Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti yum).
> Informasi lebih lanjut: <https://dnf.readthedocs.io>.

- Memperbarui seluruh paket yang terpasang ke versi terbaru:

`sudo dnf upgrade`

- Mencari paket yang tersedia dengan kata kunci tertentu:

`dnf search {{kata_kunci}}`

- Memperlihatkan informasi tentang suatu paket:

`dnf info {{nama_paket}}`

- Menginstal sebuah paket:

`sudo dnf install {{nama_paket}}`

- Menginstal sebuah paket dan jawab ya untuk semua pertanyaan:

`sudo dnf -y install {{nama_paket}}`

- Menghapus sebuah paket:

`sudo dnf remove {{nama_paket}}`

- Memperlihatkan daftar semua paket yang telah terpasang:

`dnf list --installed`

- Temukan paket mana yang menyediakan file tertentu:

`dnf provides {{file}}`
