# yarn

> Pengelola paket alternatif untuk JavaScript dan Node.js.
> Informasi lebih lanjut: <https://yarnpkg.com>.

- Memasang modul secara global:

`yarn global add {{nama_modul}}`

- Memasang semua dependensi yang dirujuk di berkas `package.json` (`install` adalah opsional):

`yarn install`

- Memasang modul dan menyimpannya sebagai dependensi ke berkas `package.json`  (tambahkan `--dev` untuk menyimpannya sebagai dependensi pengembangan):

`yarn add {{nama_modul}}@{{versi}}`

- Mencopot modul dan menghapusnya dari berkas `package.json`:

`yarn remove {{nama_modul}}`

- Membuat berkas `package.json` secara interaktif:

`yarn init`

- Mengidentifikasi apakah modul merupakan dependensi dan daftar modul lainnya yang bergantung padanya:

`yarn why {{module_name}}`
