# gitlab-runner

> Instrument CLI pentru gestionarea alergătorilor GitLab.
> Mai multe informaţii: <https://docs.gitlab.com/runner/>

- Înregistrați un alergător:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}`

- Înregistrați un alergător cu un executor Docker:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}`

- Anulează înregistrarea unui alergător:

`sudo gitlab-runner unregister --name {{name}}`

- Afișează starea serviciului de alergător:

`sudo gitlab-runner status`

- Reporniți serviciul de alergare:

`sudo gitlab-runner restart`

- Verificați dacă alergătorii înregistrați se pot conecta la GitLab:

`sudo gitlab-runner verify`
