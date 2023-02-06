# lambo new

> Egy szupererős `laravel new` a Laravel és a Valet számára. További információ: <https://github.com/tighten/lambo>.

- Hozzon létre egy új Laravel alkalmazást:

`lambo new {{app_name}}`

- Telepítse az alkalmazást egy adott elérési útvonalra:

`lambo new --path={{path/to/directory}} {{app_name}}`

- Beleértve a hitelesítési állványzatot:

`lambo new --auth {{app_name}}`

- Egy adott frontend beépítése:

`lambo new --{{vue|bootstrap|react}} {{app_name}}`

- Telepítse az npm függőségeket a projekt létrehozása után:

`lambo new --node {{app_name}}`

- Valet webhely létrehozása a projekt létrehozása után:

`lambo new --link {{app_name}}`

- Új MySQL-adatbázis létrehozása a projekttel azonos névvel:

`lambo new --create-db --dbuser={{user}} --dbpassword={{password}} {{app_name}}`

- Egy adott szerkesztő megnyitása a projekt létrehozása után:

`lambo new --editor="{{editor}}" {{app_name}}`
