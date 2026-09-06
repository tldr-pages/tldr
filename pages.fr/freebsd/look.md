# look

> Affiche les lignes commençant par un préfixe dans un fichier trié.
> Voir aussi : `grep`, `sort`.
> Plus d'informations : <https://man.freebsd.org/cgi/man.cgi?look>.

- Recherche les lignes commençant par un préfixe spécifique dans un fichier spécifique :

`look {{préfixe}} {{chemin/vers/fichier}}`

- Effectue une recherche insensible à la casse en utilisant uniquement les caractères alphanumériques :

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{préfixe}} {{chemin/vers/fichier}}`

- Spécifie un caractère de terminaison de chaîne (espace par défaut) :

`look {{[-t|--terminate]}} {{,}}`

- Recherche dans `/usr/share/dict/words` (`--ignore-case` et `--alphanum` sont activées par défaut) :

`look {{préfixe}}`
