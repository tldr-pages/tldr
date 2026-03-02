# abroot

> Utilitas yang menyediakan imutabilitas dan atomisitas penuh melalui transaksi antara 2 status partisi root (A⟺B).
> Pembaruan dilakukan menggunakan image OCI, untuk memastikan sistem selalu dalam keadaan konsisten.
> Informasi lebih lanjut: <https://docs.vanillaos.org/docs/en/abroot-manpage>.

- Tambahkan paket ke image lokal (Catatan: Setelah menjalankan perintah ini, Anda perlu menerapkan perubahan tersebut):

`sudo abroot pkg add {{package}}`

- Hapus paket dari image lokal (Catatan: Setelah menjalankan perintah ini, Anda perlu menerapkan perubahan tersebut):

`sudo abroot pkg remove {{package}}`

- Tampilkan daftar paket dalam image lokal:

`sudo abroot pkg list`

- Terapkan perubahan dalam image lokal (Catatan: Anda perlu me-reboot sistem agar perubahan ini diterapkan):

`sudo abroot pkg apply`

- Rollback sistem ke keadaan sebelumnya:

`sudo abroot rollback`

- Edit/Lihat parameter kernel:

`sudo abroot kargs {{edit|show}}`

- Tampilkan status:

`sudo abroot status`

- Tampilkan bantuan:

`abroot {{[-h|--help]}}`
