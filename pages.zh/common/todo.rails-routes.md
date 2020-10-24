# rails routes

> List routes in a Rails application.
> More information: <https://guides.rubyonrails.org/routing.html>.

- List all routes:

`rails routes`

- List all routes in an expanded format:

`rails routes --expanded`

- List routes partially matching URL helper method name, HTTP verb, or URL path:

`rails routes -g {{posts_path|GET|/posts}}`

- List routes that map to a specified controller:

`rails routes -c {{posts|Posts|Blogs::PostsController}}`
