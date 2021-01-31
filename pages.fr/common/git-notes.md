# git notes

> Ajoute ou inspecte des notes d'objets.
> Plus d'informations : <https://git-scm.com/docs/git-notes>.

- Lister toutes les notes et leurs objets rattachés :

`git notes list`

- Lister toutes les notes attaches a un objet donné :

`git notes list [{{object}}]`

- Afficher les notes attachés a un objet donné :

`git notes show [{{object}}]`

- Ajoute une note à un objet donné :

`git notes append {{object}}`

- Ajoute une note à un objet donné, en spécifiant le message :

`git notes append --message="{{message_text}}"`

- Edite une note éxistante :

`git notes edit [{{object}}]`

- Copy la note d'un objet vers un autre :

`git notes copy {{source_object}} {{objet_cible}}`

- Supprime toutes les notes d'un objet spécifié :

`git notes remove {{object}}`
