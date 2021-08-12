# rails routes

> Listați rute într-o aplicație Rails.
> Mai multe informaţii: <https://guides.rubyonrails.org/routing.html>

- Lista tuturor rutelor:

`rails routes`

- Listați toate rutele într-un format extins:

`rails routes --expanded`

- Lista rutelor care se potrivesc parțial numele metodei de ajutor URL, verbul HTTP sau calea URL:

`rails routes -g {{posts_path|GET|/posts}}`

- Lista rutelor care mapează la un controler specificat:

`rails routes -c {{posts|Posts|Blogs::PostsController}}`
