# hugo

> Generator de site-uri statice bazate pe șablon. Utilizează module, componente și teme.
> Mai multe informaţii: <https://gohugo.io>

- Creează un nou site Hugo:

`hugo new site {{path/to/site}}`

- Creați o nouă temă Hugo (teme pot fi descărcate și de la https://themes.gohugo.io/):

`hugo new theme {{theme_name}}`

- Creați o pagină nouă:

`hugo new {{section_name}}/{{filename}}`

- Construi un site la `. /public/ `director:

`hugo`

- Construiți un site care include pagini care sunt marcate ca un „proiect”:

`hugo --buildDrafts`

- Construiți un site într-un director dat:

`hugo --destination {{path/to/destination}}`

- Construiți un site, porniți un server web pentru a-l servi și reîncărcați automat atunci când paginile sunt editate:

`hugo server`
