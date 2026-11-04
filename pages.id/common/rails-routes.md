# rails routes

> Menampilkan daftar routes di aplikasi Rails.
> Informasi lebih lanjut: <https://guides.rubyonrails.org/routing.html>.

- Menampilkan semua routes:

`rails routes`

- Menampilkan semua routes dengan format yang lebih panjang:

`rails routes {{[-E|--expanded]}}`

- Menampilkan routes yang sebagian cocok dengan nama helper method URL, HTTP verb, atau path URL:

`rails routes {{[-g|--grep]}} {{posts_path|GET|/posts}}`

- Menampilkan routes yang memetakan ke controller tertentu:

`rails routes {{[-c|--controller]}} {{posts|Posts|Blogs::PostsController}}`
