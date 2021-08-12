# dokku

> Docker alimentat mini-Heroku (PaaS).
> Implementați cu ușurință mai multe aplicații pe serverul dvs. în diferite limbi utilizând o singură comandă `git-push`.
> Mai multe informaţii: <https://github.com/dokku/dokku>

- Lista aplicațiilor care rulează:

`dokku apps`

- Creați o aplicație:

`dokku apps:create {{app_name}}`

- Elimină o aplicație:

`dokku apps:destroy {{app_name}}`

- Instalați plugin-ul:

`dokku plugin:install {{full_repo_url}}`

- Legați baza de date către o aplicație:

`dokku {{db}}:link {{db_name}} {{app_name}}`
