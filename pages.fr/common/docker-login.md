# docker login

> Se connecte à un registre Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/login/>.

- Se connecte de manière interactive à un registre :

`docker login`

- Se connecte à un registre avec un nom d'utilisateur spécifique (l'utilisateur sera invité à saisir un mot de passe) :

`docker login {{[-u|--username]}} {{nom_utilisateur}}`

- Se connecte à un registre avec un nom d'utilisateur et un mot de passe spécifiques :

`docker login {{[-u|--username]}} {{nom_utilisateur}} {{[-p|--password]}} {{mot_de_passe}} {{serveur}}`

- Se connecte à un registre avec un mot de passe depuis l'entrée standard :

`echo "{{mot_de_passe}}" | docker login {{[-u|--username]}} {{nom_utilisateur}} --password-stdin`
