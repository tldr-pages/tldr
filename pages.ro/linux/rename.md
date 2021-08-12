# rename

> Redenumiți mai multe fișiere.
> NOTĂ: această pagină se referă la comanda din pachetul `util-linux`.
> Pentru versiunea Perl, a se vedea „fișier-redenumire” sau „perl-rename'.
> Avertisment: Această comandă nu are garanții și va suprascrie fișierele fără a solicita.

- Redenumiți fișierele utilizând substituții simple (înlocuiți 'foo' cu 'bar' oriunde ați găsit):

`rename {{foo}} {{bar}} {{*}}`

- Rulare uscată - afișare care redenumire ar avea loc fără a le efectua:

`rename -vn {{foo}} {{bar}} {{*}}`

- Nu suprascrieți fișierele existente:

`rename -o {{foo}} {{bar}} {{*}}`

- Schimbă extensiile de fișiere:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Prepend „foo” la toate numele de fișiere din directorul curent:

`rename {{''}} {{'foo'}} {{*}}`

- Redenumiți un grup de fișiere din ce în ce mai numerotate la zero, umplând numerele de până la 3 cifre:

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
