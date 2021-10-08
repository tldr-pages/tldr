# alias

> Créé des alias -- mots qui sont remplacés par une commande textuelle.
> Les alias expirent avec la session courante shell, sauf s'il a été défini dans le fichier de configuration shell, par exemple `~/.bashrc`.
> Plus d'informations : <https://tldp.org/LDP/abs/html/aliases.html>.

- Liste tous les alias :

`alias`

- Crée un alias générique :

`alias {{mot}}="{{commande}}"`

- Affiche la commande associée à un alias donné :

`alias {{mot}}`

- Enlève un alias :

`unalias {{mot}}`

- Transforme `rm` en une commande intéractive :

`alias {{rm}}="{{rm -i}}"`

- Crée `la` comme un raccourci de `ls -a` :

`alias {{la}}="{{ls -a}}"`
