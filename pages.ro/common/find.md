# find

> Găsește fișiere sau foldere într-un arbore de foldere, în mod recursiv.
> Vezi și: `fd`.
> Mai multe informații: <https://manned.org/find>.

- Găsește fișiere după extensie:

`find {{cale/către/folder}} -name '{{*.ext}}'`

- Găsește fișiere care se potrivesc mai multor tipare de cale/nume:

`find {{cale/către/folder}} -path '{{*/cale/*/*.ext}}' -or -name '{{*tipar*}}'`

- Găsește foldere care se potrivesc unui nume dat, în mod insensibil la majuscule:

`find {{cale/către/folder}} -type d -iname '{{*lib*}}'`

- Găsește fișiere care se potrivesc unui tipar dat, excluzând căi specifice:

`find {{cale/către/folder}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Găsește fișiere într-un interval de dimensiuni dat, limitând adâncimea recursivă la „1”:

`find {{cale/către/folder}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Rulează o comandă pentru fiecare fișier (folosește `{}` în comandă pentru a accesa numele fișierului):

`find {{cale/către/folder}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Găsește toate fișierele modificate astăzi și transmite rezultatele unei singure comenzi ca argumente:

`find {{cale/către/folder}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- Caută fișiere sau foldere goale și le șterge cu mesaje detaliate:

`find {{cale/către/folder}} -type {{f|d}} -empty -delete -print`
