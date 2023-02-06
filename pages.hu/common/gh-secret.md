# gh secret

> GitHub-titkok kezelése a parancssorból. További információk: <https://cli.github.com/manual/gh_secret>.

- Az aktuális repository titkos kulcsainak listázása:

`gh secret list`

- Egy adott szervezet titkos kulcsainak listázása:

`gh secret list --org {{organization}}`

- Egy adott tárolóhoz tartozó titkos kulcsok listázása:

`gh secret list --repo {{owner}}/{{repository}}`

- Titkos kulcsok beállítása az aktuális tárolóhoz (a felhasználónak meg kell adnia az értéket):

`gh secret set {{name}}`

- Titkos kulcsok beállítása egy fájlból az aktuális tárolóhoz:

`gh secret set {{name}} < {{path/to/file}}`

- Szervezeti titok beállítása adott adattárhoz:

`gh secret set {{name}} --org {{organization}} --repos {{repository1,repository2}}`

- Titok eltávolítása az aktuális adattárhoz:

`gh secret remove {{name}}`

- Titok eltávolítása egy adott szervezethez:

`gh secret remove {{name}} --org {{organization}}`
