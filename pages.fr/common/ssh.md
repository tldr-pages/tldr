# ssh

> Secure Shell est un protocole utilisé pour se connecter de façon sécure à des systèmes distants.
> On peut l'utiliser pour se connecter ou exécuter des commandes sur un serveur distant..

- Se connecte à un serveur distant::

`ssh {{username}}@{{remote_host}}`

- Se connecte à un serveur distant en utilisant un identité spécifique (clé privé):

`ssh -i {{path/to/key_file}} {{username}}@{{remote_host}}`

- Se connecte à un serveur distant en utilisant un port spécifique:

`ssh {{username}}@{{remote_host}} -p {{2222}}`

- Exécute une commande sur un serveur distant:

`ssh {{remote_host}} {{command -with -flags}}`

- Tunnel SSH: Transfert par port dynamique (le SOCKS proxy se trouve sur localhost:9999):

`ssh -D {{9999}} -C {{username}}@{{remote_host}}`

- Tunnel SSH: Transfère un port spécifique (localhost:9999 vers example.org:80) en désactivant l'allocation de pseudo-[t]ty et l'exécution de commandes distantes:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{username}}@{{remote_host}}`


- Saut SSH: Se connecte sur un serveur distant à travers une machine de rebond (plusieurs machines de rebond peuvent être définies en les séparant par des virgules):

`ssh -J {{username}}@{{jump_host}} {{username}}@{{remote_host}}`

- Transfer d'agent: Tranfère les informations d'authentification vers la machine distante (voir `man ssh_config` pour les options disponibles):

`ssh -A {{username}}@{{remote_host}}`
