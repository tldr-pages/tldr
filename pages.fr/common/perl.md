# perl

> Interpréteur du langage Perl (version 5).
> Plus d'informations : <https://www.perl.org>.

- Exécuter le code contenu dans un fichier :

`perl {{fichier.pl}}`

- Vérifier la syntaxe sans exécuter le programme :

`perl -c {{fichier.pl}}`

- Exécuter une expression Perl :

`perl -e {{expression}}`

- Lancer le programme avec le debugger Perl :

`perl -d {{fichier.pl}}`

- Itérer sur toutes les lignes d'un fichier, en les modifiant sur place en utilisant une expression de recherche et de remplacement :

`perl -p -i -e 's/{{recherche}}/{{remplacement}}' {{fichier}}`

- Lancer une expression de recherche et remplacement sur un fichier, en sauvegardant le fichier original avec une autre extension :

`perl -p -i'.ancien' -e 's/{{recherche}}/{{remplacement}}/g' {{fichier}}`

- Lancer une expression de recherche et remplacement sur un fichier, en sauvegardant le résultat dans un autre fichier :

`perl -p0e 's/{{recherche}}/{{remplacement}}/g' {{fichier_entrée}} > {{fichier_sortie}}`

- Lancer une expression régulière (RegEx) sur `stdin`, en affichant le premier groupe capturé pour chaque ligne :

`cat {{fichier_entrée}} | perl -nle 'if (/{{regex}}/) { print "$1"; last;}'`
