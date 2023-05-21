# ssh-keygen

> Génère des clés SSH. Utilisées entre autres pour l'authentification ou la connexion sans utiliser de mot de passe.
> Plus d'informations : <https://man.openbsd.org/ssh-keygen>.

- Génère une clé de manière interactive :

`ssh-keygen`

- Génère une clé dans un fichier spécifique :

`ssh-keygen -f {{~/.ssh/fichier}}`

- Génère une clé ed25519, avec 32 passages de fonction de dérivation de clé:

`ssh-keygen -t {{ed25519}} -a {{32}}`

- Génère une clé RSA de 4096 bits, avec l'adresse électronique en commentaire:

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{commentaire|email}}"`

- Retire les clés d'une machine donnée du fichier `known_hosts` des hôtes connus (utile lorsque un hôte déjà enregistré change de clé) :

`ssh-keygen -R {{hote_distant}}`

- Affiche l'empreinte d'une clé sous format d'un hash MD5 :

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/fichier}}`

- Change le mot de passe d'une clé :

`ssh-keygen -p -f {{~/.ssh/fichier}}`

- Change le format d'une clé (par exemple du format OPENSSH vers PEM), le fichier étant réécrit :

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/cle_privee_OpenSSH}}`
