# npm

> Manajer paket JavaScript dan Node.js.
> Mengelola proyek Node.js dan dependensi modulnya.
> Informasi lebih lanjut: <https://docs.npmjs.com/cli/npm/>.

- Membuat file `package.json` secara interaktif:

`npm init {{[-y|--yes]}}`

- Unduh semua paket yang terdaftar sebagai dependensi di package.json:

`npm {{[i|install]}}`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar dependensi di `package.json`:

`npm {{[i|install]}} {{nama_modul}}@{{versi}}`

- Unduh paket dan menambahkan ke daftar dependensi dev di package.json:

`npm {{[i|install]}} {{nama_modul}} {{[-D|--save-dev]}}`

- Unduh paket dan instal secara global:

`npm {{[i|install]}} {{nama_modul}} {{[-g|--global]}}`

- Copot pemasangan paket dan hapus dari daftar dependensi di `package.json`:

`npm {{[r|uninstall]}} {{nama_modul}}`

- Mencetak pohon dependensi yang diinstal secara lokal:

`npm {{[ls|list]}}`

- Buat daftar modul tingkat atas yang diinstal secara global:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
