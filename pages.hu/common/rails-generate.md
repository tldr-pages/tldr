# rails generate

> Új Rails sablonok generálása egy meglévő projektben. További információ: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>.

- Az összes elérhető generátor listája:

`rails generate`

- Generáljon egy új, Post nevű modellt title és body attribútumokkal:

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- Új vezérlő generálása Posts néven index, show, new és create műveletekkel:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- Generáljon egy új migrációt, amely hozzáad egy kategória attribútumot a Post nevű meglévő modellhez:

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- A Post nevű modellhez a title és body attribútumokat előre definiáló állványzat generálása:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
