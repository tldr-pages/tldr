# ftxdiff

> Két betűtípus közötti különbségek összehasonlítása. További információ: <https://developer.apple.com/fonts>.

- Különbségek kiadása egy adott szövegfájlba:

`ftxdiff --output {{path/to/fontdiff.txt}} {{path/to/font1.ttc}} {{path/to/font2.ttc}}`

- A glifák nevének felvétele a kimenetbe:

`ftxdiff --include-glyph-names`

- Unicode nevek felvétele a kimenetbe:

`ftxdiff --include-unicode-names`
