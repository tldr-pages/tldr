# pnpm

> Manajer paket JavaScript dan Node.js yang cepat dan efisien.
> Mengelola proyek Node.js dan dependensi modulnya.
> Informasi lebih lanjut: <https://pnpm.io/pnpm-cli>.

- Buat file `package.json` file:

`pnpm init`

- Unduh semua paket yang terdaftar sebagai ketergantungan/dependensi di `package.json`:

`pnpm {{[i|install]}}`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar ketergantungan di `package.json`:

`pnpm add {{nama_modul}}@{{versi}}`

- Unduh paket dan menambahkan ke daftar ketergantungan [D]ev di `package.json`:

`pnpm add {{nama_modul}} {{[-D|--save-dev]}}`

- Unduh dan pasang paket secara [g]lobal:

`pnpm add {{module_name}} {{[-g|--global]}}`

- Copot pemasangan dan hapus paket dari daftar ketergantungan dalam `package.json`:

`pnpm {{[rm|remove]}} {{module_name}}`

- Tampilkan daftar ketergantungan yang diinstal secara lokal:

`pnpm {{[ls|list]}}`

- Tampilkan daftar modul tingkat atas yang diinstal secara [g]lobal:

`pnpm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
