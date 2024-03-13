# adduser

> Utilitas penambahan pengguna.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Buat seorang pengguna baru dengan sebuah direktori pangkal/home bawaan dan mendesak pengguna untuk mengatur sebuah kata sandi:

`adduser {{nama_pengguna}}`

- Buat seorang pengguna baru tanpa sebuah direktori pangkal/home:

`adduser --no-create-home {{nama_pengguna}}`

- Buat seorang pengguna baru dengan sebuah direktori pangkal/home di jalur yang telah dispesifikasikan:

`adduser --home {{jalur/ke/home}} {{nama_pengguna}}`

- Buat seorang pengguna baru dengan shell yang telah dispesifikasikan sebagai shell login:

`adduser --shell {{jalur/ke/shell}} {{nama_pengguna}}`

- Buat seorang pengguna baru yang masuk ke grup pengguna yang dispesifikasikan:

`adduser --ingroup {{grup}} {{nama_pengguna}}`
