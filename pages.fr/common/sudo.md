# sudo

> Exécute une commande unique en tant que super-utilisateur (super-user) ou un autre utilisateur.
> Plus d'information: <https://www.sudo.ws/sudo.html>.

- Exécuter une commande en tant que super-utilisateur :

`sudo {{less /var/log/syslog}}`

- Éditer un fichier en tant que super-utilisateur avec votre éditeur par défaut:

`sudo --edit {{/etc/fstab}}`

- Exécuter une commande en tant qu'un autre utilisateur et/ou groupe :

`sudo --user={{utilisateur}} --group={{groupe}} {{id -a}}`

- Répéter la dernière commande préfixée de `sudo` (uniquement dans `bash`, `zsh`, etc.):

`sudo !!`

- Lancer le terminal par défaut avec des privilèges de super-utilisateur et exécuter des fichiers à profil spécifique (`.profile`, `.bash_profile`, etc.):

`sudo --login`

- Lancer le terminal par défaut avec des privilèges de super-utilisateur sans modifier l'environnement :

`sudo --shell`

- Lancer le terminal par défaut en tant que l'utilisateur spécifié, en chargeant l'environnement de cet utilisateur et en lisant les fichiers à profil spécifique de cet utilisateur (`.profile`, `.bash_profile`, etc.):

`sudo --login --user={{utilisateur}}`

- Lister les commandes autorisées (et interdites) pour l'utilisateur courant :

`sudo --list`
