# ssh

> Secure Shell est un protocole utilisé pour se connecter de façon sécurisée à des systèmes distants.
> On peut l'utiliser pour se connecter ou exécuter des commandes sur un serveur distant.
> Plus d'informations : <https://man.openbsd.org/ssh>.

- Se connecte à un serveur distant :

`ssh {{utilisateur}}@{{hôte_distant}}`

- Se connecte à un serveur distant en utilisant une [i]dentité spécifique (clé privée) :

`ssh {{utilisateur}}@{{hôte_distant}} -i {{chemin/vers/fichier_clé}}`

- Se connecte à un serveur distant avec IP `10.0.0.1` et utilisant un [p]ort spécifique (Remarque : `10.0.0.1` peut être réduit à `10.1`) :

`ssh {{utilisateur}}@10.0.0.1 -p {{2222}}`

- Exécute une commande sur un serveur distant avec une allocation [t]ty qui permet une interaction avec la commande distante :

`ssh {{utilisateur}}@{{hôte_distant}} -t {{commande}} {{arguments_commande}}`

- Tunnel SSH : Redirection de port [D]ynamique (le proxy SOCKS se trouve sur `localhost:1080`) :

`ssh {{utilisateur}}@{{hôte_distant}} -D {{1080}}`

- Tunnel SSH : Transfère un port spécifique (`localhost:9999` vers `example.org:80`) en désactivant l'allocation de pseudo-[T]ty et l'exécutio[N] de commandes distantes :

`ssh {{utilisateur}}@{{hôte_distant}} -L {{9999}}:{{example.org}}:{{80}} -N -T`

- Saut SSH : Se connecte à un serveur distant à travers une machine de rebond (plusieurs machines de rebond peuvent être définies en les séparant par des virgules) :

`ssh {{utilisateur}}@{{hôte_distant}} -J {{utilisateur}}@{{hôte_de_rebond}}`

- Ferme une session bloquée :

`<Enter><~><.>`
