# pnpm

> Manajer paket JavaScript dan Node.js yang cepat dan efisien.
> Mengelola proyek Node.js dan dependensi modulnya.
> Informasi lebih lanjut:: <https://pnpm.io>.

- Buat file `package.json` file:

`pnpm init`

- Unduh semua paket yang terdaftar sebagai dependensi di package.json:

`pnpm install`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar dependensi di package.json:

`pnpm add {{nama_modul}}@{{versi}}`

- Unduh paket dan menambahkan ke daftar dependensi [D]ev di package.json:

`pnpm add -D {{module_name}}`

- Unduh paket dan instal secara [g]lobal:

`pnpm add -g {{module_name}}`

- Copot pemasangan paket dan hapus dari daftar dependensi di package.json:

`pnpm remove {{module_name}}`

- Mencetak pohon dependensi yang diinstal secara lokal:

`pnpm list`

- Buat daftar modul tingkat atas yang diinstal secara [g]lobal:

`pnpm list -g --depth={{0}}`
