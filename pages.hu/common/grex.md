# grex

> Egyszerű parancssori eszköz reguláris kifejezések generálására. További információ: <https://github.com/pemistahl/grex>.

- Egyszerű reguláris kifejezés generálása:

`grex {{space_separated_strings}}`

- Nagy- és kisbetű-független reguláris kifejezés generálása:

`grex -i {{space_separated_strings}}`

- Számjegyek cseréje '\\d'-vel:

`grex -d {{space_separated_strings}}`

- Unicode szó karakterének helyettesítése '\\w'-val:

`grex -w {{space_separated_strings}}`

- Szóközök helyettesítése '\\s'-vel:

`grex -s {{space_separated_strings}}`

- {min, max} kvantifikáló ábrázolás hozzáadása az ismétlődő részláncokhoz:

`grex -r {{space_separated_strings}}`
