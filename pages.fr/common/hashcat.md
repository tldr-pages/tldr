# hashcat

> Outil de récupération de mot de passe rapide et avancé.
> Plus d'informations : <https://hashcat.net/wiki/doku.php?id=hashcat>.

- Effectue une attaque par force brute (mode 3) avec le masque hashcat par défaut :

`hashcat --hash-type {{id_type_hash}} --attack-mode {{3}} {{valeur_hash}}`

- Effectue une attaque par force brute (mode 3) avec un motif connu de 4 chiffres :

`hashcat --hash-type {{id_type_hash}} --attack-mode {{3}} {{valeur_hash}} "{{?d?d?d?d}}"`

- Effectue une attaque par force brute (mode 3) en utilisant au plus 8 caractères parmi tous les caractères ASCII imprimables :

`hashcat --hash-type {{id_type_hash}} --attack-mode {{3}} --increment {{valeur_hash}} "{{?a?a?a?a?a?a?a?a}}"`

- Effectue une attaque par dictionnaire (mode 0) en utilisant la liste de mots RockYou d'une machine Kali Linux :

`hashcat --hash-type {{id_type_hash}} --attack-mode {{0}} {{valeur_hash}} {{/usr/share/wordlists/rockyou.txt}}`

- Effectue une attaque par dictionnaire basée sur des règles (mode 0) en utilisant la liste de mots RockYou modifiée avec des variations de mots de passe courants :

`hashcat --hash-type {{id_type_hash}} --attack-mode {{0}} --rules-file {{/usr/share/hashcat/rules/best64.rule}} {{valeur_hash}} {{/usr/share/wordlists/rockyou.txt}}`

- Effectue une attaque combinée (mode 1) en utilisant la concaténation de mots provenant de deux dictionnaires personnalisés différents :

`hashcat --hash-type {{id_type_hash}} --attack-mode {{1}} {{valeur_hash}} {{/chemin/vers/dictionnaire1.txt}} {{/chemin/vers/dictionnaire2.txt}}`

- Affiche le résultat d'un hash déjà craqué :

`hashcat --show {{valeur_hash}}`
