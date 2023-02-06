# rails routes

> Útvonalak listázása egy Rails-alkalmazásban. További információ: <https://guides.rubyonrails.org/routing.html>.

- Az összes útvonal listázása:

`rails routes`

- Az összes útvonal listázása kibővített formátumban:

`rails routes --expanded`

- Az URL-segédmódszer nevének, a HTTP igének vagy az URL-útvonalnak részben megfelelő útvonalak listázása:

`rails routes -g {{posts_path|GET|/posts}}`

- A megadott vezérlőhöz tartozó útvonalak listázása:

`rails routes -c {{posts|Posts|Blogs::PostsController}}`
