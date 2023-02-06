# git sed

> Minták cseréje a git által ellenőrzött fájlokban sed segítségével. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>.

- A megadott szöveg cseréje az aktuális tárolóban:

`git sed '{{find_text}}' '{{replace_text}}'`

- A megadott szöveg cseréje, majd az így kapott változtatások commitolása egy szabványos commit üzenettel:

`git sed -c '{{find_text}}' '{{replace_text}}'`

- A megadott szöveg cseréje, reguláris kifejezések használatával:

`git sed -f g '{{find_text}}' '{{replace_text}}'`

- Egy adott szöveg cseréje egy adott könyvtár alatti összes fájlban:

`git sed '{{find_text}}' '{{replace_text}}' -- {{path/to/directory}}`
