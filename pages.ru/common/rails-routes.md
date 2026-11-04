# rails routes

> Выводить список маршрутов в приложении Rails.
> Больше информации: <https://guides.rubyonrails.org/routing.html>.

- Вывести список всех маршрутов:

`rails routes`

- Вывести список всех маршрутов в расширенном формате:

`rails routes {{[-E|--expanded]}}`

- Вывести список маршрутов, частично совпадающих с именем URL-хелпера, HTTP-методом или URL-путём:

`rails routes {{[-g|--grep]}} {{posts_path|GET|/posts}}`

- Вывести список маршрутов, связанных с конкретным контроллером:

`rails routes {{[-c|--controller]}} {{posts|Posts|Blogs::PostsController}}`
