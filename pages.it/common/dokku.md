# dokku

> Mini-Heroku basato su Docker (PaaS, Platform As A Service).
> Distribuisci facilmente molteplici app sul tuo server in diversi linguaggi utilizzando un singolo comando `git-push`.
> Maggiori informazioni: <https://dokku.com/docs/deployment/application-deployment/>.

- Elenca app in esecuzione:

`dokku apps`

- Crea un'app:

`dokku apps:create {{nome_app}}`

- Rimuovi un'app:

`dokku apps:destroy {{nome_app}}`

- Installa un plugin:

`dokku plugin:install {{url_completo_repo}}`

- Collega un database ad un'app:

`dokku {{db}}:link {{nome_db}} {{nome_app}}`
