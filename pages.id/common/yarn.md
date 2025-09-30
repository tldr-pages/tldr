# yarn

> Pengelola paket alternatif untuk JavaScript dan Node.js.
> Informasi lebih lanjut: <https://yarnpkg.com/cli>.

- Pasang suatu modul secara global:

`yarn global add {{nama_modul}}`

- Pasang semua pustaka prasyarat (dependency) yang dirujuk dalam berkas `package.json` (perintah `install` adalah opsional):

`yarn install`

- Pasang dan catat suatu modul sebagai prasyarat ke dalam berkas `package.json` (tambahkan `--dev` jika hendak menyimpannya sebagai prasyarat khusus tahap pengembangan):

`yarn add {{nama_modul}}@{{versi}}`

- Hapus pemasangan modul beserta entrinya dalam berkas `package.json`:

`yarn remove {{nama_modul}}`

- Membuat berkas `package.json` secara interaktif:

`yarn init`

- Periksa apakah suatu modul merupakan suatu prasyarat serta tampilkan daftar modul lainnya yang bergantung kepadanya:

`yarn why {{nama_modul}}`
