# composer

> Manajer paket untuk proyek PHP.
> Informasi lebih lanjut: <https://getcomposer.org/doc/03-cli.md>.

- Buat sebuah berkas `composer.json` secara interaktif:

`composer init`

- Tambahkan paket sebagai sebuah pustaka prasyarat (dependency) untuk proyek ini, menambahkan ke `composer.json`:

`composer require {{nama_pengguna/nama_paket}}`

- Pasang seluruh prasyarat dalam `composer.json` proyek ini dan buat berkas `composer.lock`:

`composer install`

- Hapus pemasangan suatu paket dalam proyek ini, sehingga menghapusnya dari entri prasyarat pada `composer.json` dan `composer.lock`:

`composer remove {{nama_pengguna/nama_paket}}`

- Perbarui semua pustaka prasyarat dalam `composer.json` proyek ini dan catat versi-versi terkini dalam berkas `composer.lock`:

`composer update`

- Memperbarui `composer.lock` setelah mengubah `composer.json` secara manual:

`composer update --lock`

- Cari tahu alasa mengapa sebuah dependensi tidak dapat dipasang:

`composer why-not {{user/nama_paket}}`

- Perbarui program composer menuju versi terbaru:

`composer self-update`
