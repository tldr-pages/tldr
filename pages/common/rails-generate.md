# rails generate

> Generate new Rails templates in an existing project.
> More information: <https://guides.rubyonrails.org/command_line.html#rails-generate>.

- List all available generators:

`rails generate`

- Generate a new model named Post with attributes title and body:

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- Generate a new controller named Posts with actions index, show, new and create:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- Generate a new migration that adds a category attribute to an existing model called Post:

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- Generate a scaffold for a model named Post, predefining the attributes title and body:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
