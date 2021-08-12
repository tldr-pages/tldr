# gh secret set

> Creați sau actualizați secretele GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_secret_set>

- Setați un secret pentru depozitul curent (utilizatorul va fi solicitat pentru valoare):

`gh secret set {{name}}`

- Setați un secret dintr-un fișier pentru depozitul curent:

`gh secret set {{name}} < {{path/to/file}}`

- Setați un secret pentru un anumit depozit:

`gh secret set {{name}} --body {{value}} --repo {{owner}}/{{repository}}`

- Setați un secret al organizației pentru anumite depozite:

`gh secret set {{name}} --org {{organization}} --repos "{{repository1,repository2,...}}"`

- Setați un secret al organizației cu o vizibilitate specifică:

`gh secret set {{name}} --org {{organization}} --visibility {{all|private|selected}}`
