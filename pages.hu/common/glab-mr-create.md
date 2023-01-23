# glab mr create

> A GitLab egyesítési kérések kezelése a parancssorból. További információ: <https://glab.readthedocs.io/en/latest/mr/create.html>.

- Interaktívan hozzon létre egy egyesítési kérelmet:

`glab mr create`

- Egyesítési kérelem létrehozása, a cím és a leírás meghatározása az aktuális ág commit üzeneteiből:

`glab mr create --fill`

- Egyesítési kérelem tervezet létrehozása:

`glab mr create --draft`

- Egyesítési kérelem létrehozása a célág, a cím és a leírás megadásával:

`glab mr create --target-branch {{target_branch}} --title "{{title}}" --description "{{description}}"`

- Egyesítési kérelem megnyitásának megkezdése az alapértelmezett webböngészőben:

`glab mr create --web`
