# rails routes

> Menampilkan daftar _routes_ di aplikasi Rails.
> Informasi lebih lanjut: <https://guides.rubyonrails.org/routing.html>.

- Menampilkan semua _routes_:

`rails routes`

- Menampilkan semua _routes_ dengan format yang lebih panjang:

`rails routes --expanded`

- Menampilkan _routes_ yang sebagian cocok dengan nama helper method URL, HTTP verb, atau path URL:

`rails routes -g {{posts_path|GET|/posts}}`

- Menampilkan _routes_ yang memetakan ke controller tertentu:

`rails routes -c {{posts|Posts|Blogs::PostsController}}`
