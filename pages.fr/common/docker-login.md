# docker login

> Se connecter à un registre Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/login/>.

- Se connecter de manière interactive à un registre :

`docker login`

- Se connecter à un registre avec un nom d'utilisateur spécifique (l'utilisateur sera invité à saisir un mot de passe) :

`docker login --username {{nom_d_utilisateur}}`

- Se connecter à un registre avec un nom d'utilisateur et un mot de passe spécifiques :

`docker login --username {{nom_d_utilisateur}} --password {{mot_de_passe}} {{serveur}}`

- Se connecter à un registre avec un mot de passe depuis l'entrée standard :

`echo "{{mot_de_passe}}" | docker login --username {{nom_d_utilisateur}} --password-stdin`
