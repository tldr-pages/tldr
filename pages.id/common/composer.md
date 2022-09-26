# composer

> Manajer paket untuk proyek PHP.
> Informasi lebih lanjut: <https://getcomposer.org/>.

- Membuat file `composer.json` secara interaktif:

`composer init`

- Menambahkan paket sebagai dependensi untuk proyek ini, menambahkan ke `composer.json`:

`composer require {{user/nama_paket}}`

- Menginstal semua dependensi dalam `composer.json` proyek ini dan membuat `composer.lock`:

`composer install`

- Menghapus sebuah paket dari proyek ini, menghapus paket tersebut sebagai ketergantungan dari `composer.json`:

`composer remove {{user/nama_paket}}`

- Memperbarui semua dependensi dalam `composer.json` proyek ini dan memperbarui versi di file `composer.lock`:

`composer update`

- Memperbarui `composer.lock` setelah mengubah `composer.json` secara manual:

`composer update --lock`

- Memcari tahu mengapa sebuah dependensi tidak dapat diinstal:

`composer why-not {{user/nama_paket}}`

- Memperbarui composer ke versi terbaru:

`composer self-update`
