# npm

> Manajer paket JavaScript dan Node.js.
> Mengelola proyek Node.js dan dependensi modulnya.
> Informasi lebih lanjut: <https://docs.npmjs.com/cli/npm/>.

- Buat berkas `package.json` dengan nilai pengaturan default (hapus `--yes` untuk membuatnya secara interaktif):

`npm init {{[-y|--yes]}}`

- Unduh semua paket yang terdaftar sebagai ketergantungan/dependency dalam package.json:

`npm {{[i|install]}}`

- Unduh versi tertentu dari sebuah paket dan menambahkan ke daftar ketergantungan di `package.json`:

`npm {{[i|install]}} {{nama_modul}}@{{versi}}`

- Unduh dan tambahkan paket ke daftar ketergantungan pengembangan (dev dependency) di package.json:

`npm {{[i|install]}} {{nama_modul}} {{[-D|--save-dev]}}`

- Unduh dan pasang paket ke secara [g]lobal:

`npm {{[i|install]}} {{nama_modul}} {{[-g|--global]}}`

- Copot pemasangan dan hapus paket dari daftar ketergantungan dalam `package.json`:

`npm {{[r|uninstall]}} {{nama_modul}}`

- Tampilkan daftar paket ketergantungan yang dipasang secara lokal:

`npm {{[ls|list]}}`

- Tampilkan daftar paket tingkat atas yang diinstal secara global:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
