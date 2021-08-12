# rename

> Redenumiți mai multe fișiere.
> NOTĂ: această pagină se referă la comanda din pachetul `prename` Fedora.

- Redenumiți fișierele utilizând o expresie regulată Perl (înlocuiți „foo” cu „bar” oriunde ați găsit):

`rename {{'s/foo/bar/'}} {{*}}`

- Rulare uscată - afișare care redenumire ar avea loc fără a le efectua:

`rename -n {{'s/foo/bar/'}} {{*}}`

- Forțați redenumirea chiar dacă operațiunea ar elimina fișierele de destinație existente:

`rename -f {{'s/foo/bar/'}} {{*}}`

- Convertiți numele fișierelor în minuscule (utilizați `-f` în sistemele de fișiere insensibile la majuscule pentru a preveni erorile „deja există”):

`rename 'y/A-Z/a-z/' {{*}}`

- Înlocuiți spațiul alb cu sublinieri:

`rename 's/\s+/_/g' {{*}}`
