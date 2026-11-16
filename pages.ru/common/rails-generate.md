# rails generate

> Генерировать новые шаблоны Rails в существующем проекте.
> Больше информации: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- Вывести список всех доступных генераторов:

`rails generate`

- Сгенерировать новую модель Post с атрибутами title и body:

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- Сгенерировать новый контроллер Posts с действиями index, show, new и create:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- Сгенерировать новую миграцию, добавляющую атрибут category в существующую модель Post:

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- Сгенерировать каркас для модели Post, задав атрибуты title и body:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
