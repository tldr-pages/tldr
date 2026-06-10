# gitlab-runner

> Կառավարեք GitLab-ի վազորդները:.
> Լրացուցիչ տեղեկություններ. <https://docs.gitlab.com/runner/>:.

- Գրանցեք վազորդ.:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}`

- Գրանցեք վազորդ Docker կատարողի հետ.:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}`

- Չեղարկել վազորդի գրանցումը.:

`sudo gitlab-runner unregister --name {{name}}`

- Ցուցադրել վազող ծառայության կարգավիճակը.:

`sudo gitlab-runner status`

- Վերագործարկեք runner ծառայությունը.:

`sudo gitlab-runner restart`

- Ստուգեք, արդյոք գրանցված վազորդները կարող են միանալ GitLab-ին.:

`sudo gitlab-runner verify`
