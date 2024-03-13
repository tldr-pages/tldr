# adduser

> Utilitas penambahan pengguna.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Buat seorang pengguna baru dengan sebuah direktori home bawaan dan mendesak pengguna untuk mengatur sebuah password:

`adduser {{nama_pengguna}}`

- Buat seorang pengguna baru tanpa sebuah direktori home:

`adduser --no-create-home {{nama_pengguna}}`

- Buat seorang pengguna baru dengan sebuah direktori home di jalur yang telah dispesifikasikan:

`adduser --home {{jalur/ke/home}} {{nama_pengguna}}`

- Buat seorang pengguna baru dengan shell yang telah dispesifikasikan sebagai shell login:

`adduser --shell {{jalur/ke/shell}} {{nama_pengguna}}`

- Buat seorang pengguna baru yang masuk ke grup yang dispesifikasikan:

`adduser --ingroup {{grup}} {{nama_pengguna}}`
