# dokku

> Docker-alapú mini-Heroku (PaaS). Könnyen telepíthet több alkalmazást a szerverére különböző nyelveken egyetlen `git-push` paranccsal. További információ: <https://github.com/dokku/dokku>.

- Futtatott alkalmazások listázása:

`dokku apps`

- Hozzon létre egy alkalmazást:

`dokku apps:create {{app_name}}`

- Alkalmazás eltávolítása:

`dokku apps:destroy {{app_name}}`

- Plugin telepítése:

`dokku plugin:install {{full_repo_url}}`

- Adatbázis összekapcsolása egy alkalmazással:

`dokku {{db}}:link {{db_name}} {{app_name}}`
