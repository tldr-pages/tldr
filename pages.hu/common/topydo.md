# topydo

> A todo.txt formátumot használó feladatlista alkalmazás. További információ: <https://github.com/topydo/topydo>.

- Egy adott kontextusú projekthez hozzáad egy tennivalót:

`topydo add "{{todo_message}} +{{project_name}} @{{context_name}}"`

- Feladat hozzáadása holnapi esedékességgel és `A` prioritással:

`topydo add "(A) {{todo _message}} due:{{1d}}"`

- Pénteki esedékességű tennivaló hozzáadása:

`topydo add "{{todo_message}} due:{{fri}}"`

- Nem szigorúan ismétlődő feladat hozzáadása (következő esedékesség = most + rec):

`topydo add "water flowers due:{{mon}} rec:{{1w}}"`

- Szigorúan ismétlődő feladat hozzáadása (következő esedékesség = jelenlegi esedékesség + rec):

`topydo add "{{todo_message}} due:{{2020-01-01}} rec:{{+1m}}"`

- A legutóbb végrehajtott `topydo` parancs visszavonása:

`topydo revert`
