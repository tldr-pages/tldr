# john

> Outil de cassage de mot de passe.
> Plus d'informations : <https://www.openwall.com/john/>.

- Craque les hashs de mots de passe :

`john {{chemin/vers/hashs.txt}}`

- Affiche les mots de passe cassés :

`john --show {{chemin/vers/hashs.txt}}`

- Affiche les mots de passe cassés des utilisateurs par identifiant d'utilisateur à partir de plusieurs fichiers :

`john --show --users={{ids_utilisateurs}} {{chemin/vers/hashs*}} {{chemin/vers/autres/hashs*}}`

- Craque des hashs de mots de passe, à l'aide d'une liste de mots personnalisée :

`john --wordlist={{chemin/vers/liste_de_mots.txt}} {{chemin/vers/hashs.txt}}`

- Liste des formats de hachage disponibles :

`john --list=formats`

- Craque les hashs de mots de passe, en utilisant un format de hash spécifique :

`john --format={{md5crypt}} {{chemin/vers/hashs.txt}}`

- Craque les hashs de mots de passe, en activant les règles d'altération de mots :

`john --rules {{chemin/vers/hashs.txt}}`

- Restaure une session de craquage interrompue à partir d'un fichier d'état, par exemple `mon_cassage.rec` :

`john --restore={{chemin/vers/mon_cassage.rec}}`
