# dnf

> Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti yum).
> Informasi lebih lanjut: <https://dnf.readthedocs.io>.

- Memperbarui seluruh paket yang terpasang ke versi terbaru:

`sudo dnf upgrade`

- Mencari paket yang tersedia dengan kata kunci tertentu:

`dnf search {{kata_kunci1 kata_kunci2 ...}}`

- Memperlihatkan informasi tentang suatu paket:

`dnf info {{paket}}`

- Menginstal sebuah paket (gunakan `-y` jawab untuk ya semua pertanyaan):

`sudo dnf install {{paket1 paket2 ...}}`

- Menghapus sebuah paket:

`sudo dnf remove {{paket1 paket2 ...}}`

- Memperlihatkan daftar semua paket yang telah terpasang:

`dnf list --installed`

- Temukan paket mana yang menyediakan file tertentu:

`dnf provides {{file}}`
