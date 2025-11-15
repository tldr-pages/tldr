# docker login

> Se connecter à un registre Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/login/>.

- Se connecter de manière interactive à un registre :

`docker login`

- Se connecter à un registre avec un nom d'utilisateur spécifique (l'utilisateur sera invité à saisir un mot de passe) :

`docker login {{[-u|--username]}} {{nom_d_utilisateur}}`

- Se connecter à un registre avec un nom d'utilisateur et un mot de passe spécifiques :

`docker login {{[-u|--username]}} {{nom_d_utilisateur}} {{[-p|--password]}} {{mot_de_passe}} {{serveur}}`

- Se connecter à un registre avec un mot de passe depuis l'entrée standard :

`echo "{{mot_de_passe}}" | docker login {{[-u|--username]}} {{nom_d_utilisateur}} --password-stdin`
