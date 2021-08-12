# find

> Găsiți fișiere sau directoare sub arborele de directoare dat, recursiv.
> Mai multe informaţii: <https://manned.org/find>

- Găsiți fișiere prin extensie:

`find {{root_path}} -name '{{*.ext}}'`

- Găsiți fișiere care se potrivesc cu mai multe modele de cale/nume:

`find {{root_path}} -path '{{**/path/**/*.ext}} -or -name '{{*pattern*}}'`

- Găsiți directoare care se potrivesc unui anumit nume, în modul insensibil la minuscule:

`find {{root_path}} -type d -iname '{{*lib*}}'`

- Găsiți fișiere care se potrivesc unui model dat, excluzând anumite căi:

`find {{root_path}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Găsiți fișiere care se potrivesc unui interval de dimensiuni dat:

`find {{root_path}} -size {{+500k}} -size {{-10M}}`

- Rulați o comandă pentru fiecare fișier (utilizați `{}` în cadrul comenzii pentru a accesa numele fișierului):

`find {{root_path}} -name '{{*.ext}}' -exec {{wc -l {} }}\;`

- Găsiți fișiere modificate în ultimele 7 zile și ștergeți-le:

`find {{root_path}} -mtime -{{7}} -delete`

- Găsiți fișiere goale (0 octet) și ștergeți-le:

`find {{root_path}} -type {{f}} -empty -delete`
