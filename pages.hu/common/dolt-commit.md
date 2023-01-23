# dolt commit

> A táblázatok szakaszos módosításainak rögzítése. További információ: <https://docs.dolthub.com/interfaces/cli#dolt-commit>.

- Az összes szakaszos változtatás rögzítése, a `$EDITOR` által megadott szerkesztő megnyitásával a rögzítési üzenet beírásához:

`dolt commit`

- Az összes szakaszos változtatás rögzítése a megadott üzenettel:

`dolt commit --message "{{commit_message}}"`

- A táblázatok összes szakaszolatlan módosításának szakaszolása a kötelezettségvállalás előtt:

`dolt commit --all`

- Használja a megadott ISO 8601 commit dátumot (alapértelmezett az aktuális dátum és idő):

`dolt commit --date "{{2021-12-31T00:00:00}}"`

- A megadott szerzőt használja a kötelezettségvállaláshoz:

`dolt commit --author "{{author_name}} <{{author_email}}>"`

- Engedélyezi üres, változtatás nélküli commit létrehozását:

`dolt commit --allow-empty`

- Idegen kulcsokra vonatkozó figyelmeztetések figyelmen kívül hagyása:

`dolt commit --force`
