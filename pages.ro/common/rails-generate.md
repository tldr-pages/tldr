# rails generate

> Generați șabloane de șine noi într-un proiect existent.
> Mai multe informaţii: <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>

- Listează toate generatoarele disponibile:

`rails generate`

- Generați un nou model numit Post cu atribute titlu și corp:

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- Generați un nou controler numit Posturi cu index de acțiuni, arată, nou și de a crea:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- Generați o nouă migrare care adaugă un atribut de categorie la un model existent numit Post:

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- Generați o schelă pentru un model numit Post, predefinind titlul și corpul atributelor:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
