# lambo new

> Un super-alimentat `laravel nou` pentru Laravel și Valet.
> Mai multe informaţii: <https://github.com/tighten/lambo>

- Creați o nouă aplicație Laravel:

`lambo new {{app_name}}`

- Instalați aplicația într-o anumită cale:

`lambo new --path={{path/to/directory}} {{app_name}}`

- Include schele de autentificare:

`lambo new --auth {{app_name}}`

- Includeți o anumită interfață:

`lambo new --{{vue|bootstrap|react}} {{app_name}}`

- Instalați dependențe npm după ce proiectul a fost creat:

`lambo new --node {{app_name}}`

- Creați un site Valet după ce proiectul a fost creat:

`lambo new --link {{app_name}}`

- Creați o nouă bază de date MySQL cu același nume ca și proiectul:

`lambo new --create-db --dbuser={{user}} --dbpassword={{password}} {{app_name}}`

- Deschideți un editor specific după ce proiectul a fost creat:

`lambo new --editor="{{editor}}" {{app_name}}`
