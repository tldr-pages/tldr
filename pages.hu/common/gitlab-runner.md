# gitlab-runner

> CLI eszköz a GitLab futók kezelésére. További információ: <https://docs.gitlab.com/runner/>.

- Regisztráljon egy futót:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}`

- Regisztráljon egy futót egy Docker végrehajtóhoz:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}`

- Egy futó leregisztrálása:

`sudo gitlab-runner unregister --name {{name}}`

- A futószolgáltatás állapotának megjelenítése:

`sudo gitlab-runner status`

- A futószolgáltatás újraindítása:

`sudo gitlab-runner restart`

- Ellenőrizze, hogy a regisztrált futók tudnak-e csatlakozni a GitLabhoz:

`sudo gitlab-runner verify`
