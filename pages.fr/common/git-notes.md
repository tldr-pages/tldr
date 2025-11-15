# git notes

> Ajoute ou inspecte des notes d'objets.
> Plus d'informations : <https://git-scm.com/docs/git-notes>.

- Lister toutes les notes et leurs objets rattachés :

`git notes list`

- Lister toutes les notes attachées à un objet donné :

`git notes list [{{objet}}]`

- Afficher les notes attachées à un objet donné :

`git notes show [{{objet}}]`

- Ajoute une note à un objet donné :

`git notes append {{objet}}`

- Ajoute une note à un objet donné, en spécifiant le message :

`git notes append --message="{{texte_du_message}}"`

- Édite une note existante :

`git notes edit [{{objet}}]`

- Copie la note d'un objet vers un autre :

`git notes copy {{objet_source}} {{objet_cible}}`

- Supprime toutes les notes d'un objet donné :

`git notes remove {{objet}}`
