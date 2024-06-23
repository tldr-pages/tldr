# sudo

> Exécute une commande unique en tant que super-utilisateur (super-user) ou un autre utilisateur.
> Plus d'informations : <https://www.sudo.ws/sudo.html>.

- Exécute une commande en tant que super-utilisateur :

`sudo {{less /var/log/syslog}}`

- Édite un fichier en tant que super-utilisateur avec votre éditeur par défaut :

`sudo --edit {{/etc/fstab}}`

- Exécute une commande en tant qu'un autre utilisateur et/ou groupe :

`sudo --user={{utilisateur}} --group={{groupe}} {{id -a}}`

- Répéte la dernière commande préfixée de `sudo` (uniquement dans Bash, Zsh, etc.) :

`sudo !!`

- Lance le terminal par défaut avec des privilèges de super-utilisateur et exécuter des fichiers à profil spécifique (`.profile`, `.bash_profile`, etc.) :

`sudo --login`

- Lance le terminal par défaut avec des privilèges de super-utilisateur sans modifier l'environnement :

`sudo --shell`

- Lance le terminal par défaut en tant que l'utilisateur spécifié, en chargeant l'environnement de cet utilisateur et en lisant les fichiers à profil spécifique de cet utilisateur (`.profile`, `.bash_profile`, etc.) :

`sudo --login --user={{utilisateur}}`

- Liste les commandes autorisées (et interdites) pour l'utilisateur courant :

`sudo --list`
