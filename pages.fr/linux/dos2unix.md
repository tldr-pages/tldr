# dos2unix

> Remplace les fins de lignes de style DOS par des fins de lignes de style Unix.
> Remplace CRLF par LF.
> Voir également `unix2dos`, `unix2mac`, et `mac2unix`.
> Plus d'informations : <https://manned.org/dos2unix>.

- Remplace les fins de lignes d'un fichier :

`dos2unix {{chemin/vers/fichier}}`

- Crée une copie avec des fins de lignes de type Unix :

`dos2unix {{[-n|--newfile]}} {{chemin/vers/fichier}} {{chemin/vers/nouveau_fichier}}`

- Affiche les informations d'un fichier :

`dos2unix {{[-i|--info]}} {{chemin/vers/fichier}}`

- Conserve/Ecrit/Supprime la marque d'ordre des octets (BOM) :

`dos2unix --{{keep-bom|add-bom|remove-bom}} {{chemin/vers/fichier}}`
