# choice

> Felkéri a felhasználót egy választás kiválasztására, és visszaadja a kiválasztott választás indexét. További információ: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/choice>.

- Az aktuális felhasználót a `Y` vagy a `N` választási lehetőség kiválasztására kéri:

`choice`

- Az aktuális felhasználót arra kéri, hogy válasszon egy \[c\]választást egy adott készletből:

`choice /c {{AB}}`

- Az aktuális felhasználót egy adott \[m\]esszét tartalmazó választás kiválasztására szólítja fel:

`choice /m "{{message}}"`

- Az aktuális felhasználót egy \[c\]ase-\[s\]ensitive \[c\]hoice kiválasztására kéri egy adott készletből:

`choice /cs /c {{Ab}}`

- Az aktuális felhasználót egy választás kiválasztására és a \[d\]efault választás előnyben részesítésére kéri egy adott \[t\]ime alatt:

`choice /t {{5}} /d {{N}}`

- Súgó megjelenítése:

`choice /?`
