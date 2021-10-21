# rails generate

> Membuat Rails templates yang baru ke suatu proyek.
> Informasi lebih lanjut: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- Menampilkan semua generator yang tersedia:

`rails generate`

- Membuat model baru bernama Post dengan atribut judul dan uraian:

`rails generate model {{Post}} {{judul:string}} {{uraian:text}}`

- Mmebuat _controller_ baru bernama Posts dengan actions index, show, new dan create:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- Membuat migrasi baru yang menambahkan atribut kategori ke model yang sudah ada bernama Post:

`rails generate migration {{AddKategoriToPost}} {{kategori:string}}`

- Membuat _scaffold_ untuk model bernama Post, dengan pendefinisian atribut judul dan uraian:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
