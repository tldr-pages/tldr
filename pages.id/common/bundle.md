# bundle

> Manajer paket dan ketergantungan untuk bahasa pemrograman Ruby.
> Informasi lebih lanjut: <https://bundler.io/man/bundle.1.html>.

- Pasang seluruh gem (paket) yang terdaftar dalam berkas `Gemfile` yang diharapkan tersedia dalam direktori kerja saat ini:

`bundle install`

- Jalankan suatu perintah dalam konteks lingkungan pemasangan paket Ruby saat ini:

`bundle exec {{perintah}} {{kumpulan_argumen_perintah}}`

- Perbarui seluruh gem menurut aturan ketergantungan dalam berkas `Gemfile` dan bangun ulang berkas `Gemfile.lock`:

`bundle update`

- Perbarui satu atau beberapa gem yang terdaftar dalam berkas `Gemfile`:

`bundle update {{nama_gem1 nama_gem2 ...}}`

- Hanya perbarui kumpulan gem `Gemfile` menuju versi patch/minor berikutnya:

`bundle update --patch {{nama_gem1 nama_gem2 ...}}`

- Perbarui seluruh gem dalam grup ketergantungan tertentu dalam `Gemfile`:

`bundle update --group {{development}}`

- Tampilkan kumpulan gem yang terpasang dalam `Gemfile` beserta versi terbaru yang tersedia untuk pemutakhiran:

`bundle outdated`

- Buat suatu kerangka paket/gem baru:

`bundle gem {{nama_gem}}`
