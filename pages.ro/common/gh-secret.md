# gh secret

> Gestionați secretele GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_secret>

- Lista cheilor secrete pentru depozitul curent:

`gh secret list`

- Lista cheilor secrete pentru o anumită organizație:

`gh secret list --org {{organization}}`

- Lista cheilor secrete pentru un anumit depozit:

`gh secret list --repo {{owner}}/{{repository}}`

- Setați un secret pentru depozitul curent (utilizatorul va fi solicitat pentru valoare):

`gh secret set {{name}}`

- Setați un secret dintr-un fișier pentru depozitul curent:

`gh secret set {{name}} < {{path/to/file}}`

- Setați un secret al organizației pentru anumite depozite:

`gh secret set {{name}} --org {{organization}} --repos {{repository1,repository2}}`

- Eliminați un secret pentru depozitul curent:

`gh secret remove {{name}}`

- Eliminați un secret pentru o anumită organizație:

`gh secret remove {{name}} --org {{organization}}`
