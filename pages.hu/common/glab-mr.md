# glab mr

> A GitLab egyesítési kérések kezelése a parancssorból. Néhány alparancsnak, mint például a `glab mr create`, saját használati dokumentációja van. További információ: <https://glab.readthedocs.io/en/latest/mr>.

- Egyesítési kérelem létrehozása:

`glab mr create`

- Egy adott egyesítési kérelem helyi ellenőrzése:

`glab mr checkout {{mr_number}}`

- Az egyesítési kérelemben végrehajtott változtatások megtekintése:

`glab mr diff`

- Az aktuális ág egyesítési kérelmének jóváhagyása:

`glab mr approve`

- Az aktuális ághoz tartozó egyesítési kérelem interaktív egyesítése:

`glab mr merge`

- Egyesítési kérelem interaktív szerkesztése:

`glab mr update`

- Az egyesítési kérelem célágának szerkesztése:

`glab mr update --target-branch {{branch_name}}`
