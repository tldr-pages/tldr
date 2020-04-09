# rails generate

> Generate new Rails templates in an existing project.
> More information: <https://guides.rubyonrails.org/command_line.html#rails-generate>.

- List all available generators:

`rails generate`

- Generate a new model with attributes:

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- Generate a new controller with several actions:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- Generate a new migration that adds an attribute to an existing model:

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- Generate a scaffold for a new model with pre-defined attributes:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
