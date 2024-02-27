# hexyl

> Un simple visualiseur hexadécimal pour le terminal. Il utilise des couleurs pour distinguer les différentes catégories d'octets.
> Plus d'informations : <https://github.com/sharkdp/hexyl>.

- Affiche la représentation hexadécimale d'un fichier :

`hexyl {{chemin/vers/fichier}}`

- Affiche la représentation hexadécimale des n premiers octets d'un fichier :

`hexyl -n {{n}} {{chemin/vers/fichier}}`

- Affiche les octets 512 à 1024 d'un fichier :

`hexyl -r {{512}}:{{1024}} {{chemin/vers/fichier}}`

- Affiche 512 octets en commençant par le 1024e octet :

`hexyl -r {{1024}}:+{{512}} {{chemin/vers/fichier}}`
