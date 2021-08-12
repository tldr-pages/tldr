# gitlab-ctl

> Instrumentul CLI pentru gestionarea omnibusului GitLab.
> Mai multe informaţii: <https://docs.gitlab.com/omnibus/maintenance/>

- Afișează starea fiecărui serviciu:

`sudo gitlab-ctl status`

- Afișați starea unui anumit serviciu:

`sudo gitlab-ctl status {{nginx}}`

- Reporniți fiecare serviciu:

`sudo gitlab-ctl restart`

- Reporniți un anumit serviciu:

`sudo gitlab-ctl restart {{nginx}}`

- Afișați jurnalele fiecărui serviciu și continuați să citiți până când este apăsat „Ctrl + C”:

`sudo gitlab-ctl tail`

- Afișează jurnalele unui anumit serviciu:

`sudo gitlab-ctl tail {{nginx}}`
