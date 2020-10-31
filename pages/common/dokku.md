# dokku

> Docker powered mini-Heroku (PaaS).
> Easily deploy multiple apps to your server in different languages using a single `git-push` command.
> More information: <https://github.com/dokku/dokku>.

- List running apps:

`dokku apps`

- Create an app:

`dokku apps:create {{app_name}}`

- Remove an app:

`dokku apps:destroy {{app_name}}`

- Install plugin:

`dokku plugin:install {{full_repo_url}}`

- Link database to an app:

`dokku {{db}}:link {{db_name}} {{app_name}}`
