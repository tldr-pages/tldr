# imgp

> JPEG és PNG képek parancssoros képátalakítója és -forgatója. További információ: <https://github.com/jarun/imgp>.

- Egyedi képek és/vagy egész, érvényes képformátumokat tartalmazó könyvtárak konvertálása:

`imgp -x {{1366x1000}} {{path/to/directory}} {{path/to/file}}`

- Egy kép 75%-os méretezése és a forráskép felülírása a célfelbontásra:

`imgp -x {{75}} -w {{path/to/file}}`

- Egy kép elforgatása az óramutató járásával megegyező irányban 90 fokkal:

`imgp -o {{90}} {{path/to/file}}`
