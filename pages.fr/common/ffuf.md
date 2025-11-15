# ffuf

> Un outil d'énumération web rapide écrit en Go.
> Le mot-clé `FUZZ` est utilisé comme substitut. `ffuf` essaiera d'atteindre l'URL en remplaçant le mot `FUZZ` par tous les mots de la liste donnée.
> Plus d'informations : <https://github.com/ffuf/ffuf#usage>.

- Énumère les répertoires en utilisant une sortie [c]olorée et une liste ([w]ordlist) spécifiant une [u]RL cible :

`ffuf -c -w {{chemin/vers/liste.txt}} -u {{http://cible/FUZZ}}`

- Énumère les sous-domaines en changeant la position du mot-clé :

`ffuf -w {{chemin/vers/sous-domaines.txt}} -u {{http://FUZZ.cible.com}}`

- Énumère avec le nombre de fils d'exécution ([t]hreads) spécifié (par défaut : 40) et passe le trafic par un serveur mandataire (pro[x]y) et sauvegarde la sortie ([o]utput) dans un fichier :

`ffuf -o -w {{chemin/vers/liste.txt}} -u {{http://cible/FUZZ}} -t {{500}} -x {{http://127.0.0.1:8080}}`

- Énumère dans un en-tête ([H]eader) spécifique ("Nom : Valeur") et n'affiche que les [c]odes d'état HTTP correspondant ([m]atch) :

`ffuf -w {{chemin/vers/liste.txt}} -u {{http://cible.com}} -H "{{Host: FUZZ}}" -mc {{200}}`

- Énumère en spécifiant une méthode HTTP spécifiée et des [d]onnées, tout en [f]iltrant les [c]odes d'état séparés par des virgules :

`ffuf -w {{chemin/vers/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{http://cible/login.php}} -fc {{401,403}}`
