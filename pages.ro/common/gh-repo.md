# gh repo

> Lucrul cu depozitele GitHub în linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_repo>

- Creați un nou depozit (dacă numele depozitului nu este setat, numele implicit va fi numele directorului curent):

`gh repo create {{name}}`

- Clonează un depozit:

`gh repo clone {{owner}}/{{repository}}`

- Furculiță și clona un depozit:

`gh repo fork {{owner}}/{{repository}} --clone`

- Vizualizați un depozit în browserul web:

`gh repo view {{repository}} --web`

- Lista depozitelor deținute de un anumit utilizator sau organizație (în cazul în care proprietarul nu este setat, proprietarul implicit va fi utilizatorul autentificat în prezent):

`gh repo list {{owner}}`

- Se enumeră numai depozitele nefurculițe:

`gh repo list {{owner}} --non-forks`

- Lista depozitelor cu un limbaj specific de codificare primară:

`gh repo list {{owner}} --language {{language_name}}`
