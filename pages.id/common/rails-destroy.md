# rails destroy

> Menghapus sumber daya (resources) yang dikelola dalam suatu proyek Rails.
> Informasi lebih lanjut: <https://guides.rubyonrails.org/command_line.html#bin-rails-destroy>.

- Tampilkan daftar semua generator yang tersedia untuk membantu proses penghapusan:

`rails destroy`

- Hapus suatu model yang bernama Post:

`rails destroy model {{Post}}`

- Hapus suatu controller yang bernama Posts:

`rails destroy controller {{Posts}}`

- Hapus suatu migrasi yang membuat Posts:

`rails destroy migration {{CreatePosts}}`

- Hapus suatu scaffold bagi model Post:

`rails destroy scaffold {{Post}}`
