# idnits

> Verificați proiectele de internet pentru nits de depunere.
> Caută încălcări ale secțiunilor 2.1 și 2.2 din cerințele enumerate pe  <https://www.ietf.org/id-info/checklist>.
> Mai multe informaţii: <https://tools.ietf.org/tools/idnits/>

- Verificați un fișier pentru nits:

`idnits {{path/to/file.txt}}`

- Numără nits fără a le afișa:

`idnits --nitcount {{path/to/file.txt}}`

- Afișați informații suplimentare despre liniile ofensatoare:

`idnits --verbose {{path/to/file.txt}}`

- Așteptați anul specificat în boilerplate în loc de anul curent:

`idnits --year {{2021}} {{path/to/file.txt}}`

- Să presupunem că documentul are statutul specificat:

`idnits --doctype {{standard|informational|experimental|bcp|ps|ds}} {{path/to/file.txt}}`
