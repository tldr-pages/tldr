# npm

> Manajer paket JavaScript dan Node.js.
> Mengelola proyek Node.js dan dependensi modulnya.
> Informasi lebih lanjut: <https://www.npmjs.com>.

- Membuat file `package.json` secara interaktif:

`npm init`

- Unduh semua paket yang terdaftar sebagai dependensi di package.json:

`npm install`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar dependensi di `package.json`:

`npm install {{nama_modul}}@{{versi}}`

- Unduh paket dan menambahkan ke daftar dependensi dev di package.json:

`npm install {{nama_modul}} --save-dev`

- Unduh paket dan instal secara global:

`npm install --global {{nama_modul}}`

- Copot pemasangan paket dan hapus dari daftar dependensi di `package.json`:

`npm uninstall {{nama_modul}}`

- Mencetak pohon dependensi yang diinstal secara lokal:

`npm list`

- Buat daftar modul tingkat atas yang diinstal secara global:

`npm list --global --depth={{0}}`
