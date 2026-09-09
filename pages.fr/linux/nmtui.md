# nmtui

> Interface utilisateur textuelle pour contrôler NetworkManager.
> Utiliser les `<ArrowKeys>` pour naviguer, et `<Enter>` pour sélectionner une option.
> Voir aussi : `nmcli`.
> Plus d'informations : <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Ouvre l’interface utilisateur :

`nmtui`

- Liste les connexions disponibles, avec la possibilité de les activer ou de les désactiver :

`nmtui connect`

- Se connecte à un réseau donné :

`nmtui connect {{nom|uuid|périphérique|ssid}}`

- Modifie/Ajoute/Supprime un réseau donné :

`nmtui edit {{nom|id}}`

- Définit le nom d’hôte du système :

`nmtui hostname`
