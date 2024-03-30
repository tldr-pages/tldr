# rails db

> Beragam subperintah yang berkaitan dengan database untuk Rauby on Rails.
> Informasi lebih lanjut: <https://guides.rubyonrails.org/command_line.html>.

- Buat pangkalan data (database) baru, memuat skema dan menginisiasinya dengan data awal:

`rails db:setup`

- Akses konsol database:

`rails db`

- Buat database yang didefinisikan di environment saat ini:

`rails db:create`

- Hapus database yang didefinisikan di environment saat ini:

`rails db:drop`

- Jalankan migrasi yang belum:

`rails db:migrate`

- Tampilkan status dari masing-masing file migrasi:

`rails db:migrate:status`

- Rollback ke migrasi sebelumnya:

`rails db:rollback`

- Isi database dengan data yang didefinisikan di `db/seeds.rb`:

`rails db:seed`
