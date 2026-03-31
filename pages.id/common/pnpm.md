# pnpm

> Manajer paket JavaScript dan Node.js yang cepat dan efisien.
> Mengelola proyek Node.js dan dependensi modulnya.
> Informasi lebih lanjut: <https://pnpm.io/pnpm-cli>.

- Buat file `package.json` file:

`pnpm init`

- Unduh semua paket yang terdaftar sebagai dependensi di `package.json`:

`pnpm {{[i|install]}}`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar dependensi di `package.json`:

`pnpm add {{nama_modul}}@{{versi}}`

- Unduh paket dan menambahkan ke daftar dependensi [D]ev di `package.json`:

`pnpm add {{module_name}} {{[-D|--save-dev]}}`

- Unduh paket dan instal secara [g]lobal:

`pnpm add {{module_name}} {{[-g|--global]}}`

- Copot pemasangan paket dan hapus dari daftar dependensi di `package.json`:

`pnpm {{[rm|remove]}} {{module_name}}`

- Mencetak pohon dependensi yang diinstal secara lokal:

`pnpm {{[ls|list]}}`

- Buat daftar modul tingkat atas yang diinstal secara [g]lobal:

`pnpm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
