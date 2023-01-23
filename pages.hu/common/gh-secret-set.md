# gh secret set

> GitHub-titkok létrehozása vagy frissítése a parancssorból. További információk: <https://cli.github.com/manual/gh_secret_set>.

- Titok beállítása az aktuális tárolóhoz (a felhasználónak meg kell adnia az értéket):

`gh secret set {{name}}`

- Titok beállítása egy fájlból az aktuális tárolóhoz:

`gh secret set {{name}} < {{path/to/file}}`

- Titok beállítása egy adott tárolóhoz:

`gh secret set {{name}} --body {{value}} --repo {{owner}}/{{repository}}`

- Szervezeti titok beállítása adott tárolókhoz:

`gh secret set {{name}} --org {{organization}} --repos "{{repository1,repository2,...}}"`

- Szervezeti titok beállítása meghatározott láthatósággal:

`gh secret set {{name}} --org {{organization}} --visibility {{all|private|selected}}`
