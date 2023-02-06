# crunch

> Szólista generátor. További információ: <https://sourceforge.net/projects/crunch-wordlist/>.

- 1-től 3-ig terjedő hosszúságú, csak kisbetűket tartalmazó szavak listájának kimenete:

`crunch {{1}} {{3}}`

- 8 hosszúságú hexadecimális szavak listájának kimenete:

`crunch {{8}} {{8}} {{0123456789abcdef}}`

- Az abc összes permutációjának listájának kimenete (a hosszúságok nem kerülnek feldolgozásra):

`crunch {{1}} {{1}} -p {{abc}}`

- A megadott karakterláncok összes permutációjának listája (a hosszúságok nem kerülnek feldolgozásra):

`crunch {{1}} {{1}} -p {{abc}} {{def}} {{ghi}}`

- A megadott minta szerint generált szavak listájának kimenete és a duplikált betűk maximális száma:

`crunch {{5}} {{5}} {{abcde123}} -t {{@@@12}} -d 2@`

- A szavak listájának kiírása adott méretű darabos fájlokban, az adott karakterlánccal kezdve:

`crunch {{3}} {{5}} -o {{START}} -b {{10kb}} -s {{abc}}`

- A szavak listájának kiírása a megadott karakterlánccal befejezve és a szólistát megfordítva:

`crunch {{1}} {{5}} -o {{START}} -e {{abcde}} -i`

- Szavak listájának írása tömörített darabos fájlokban, megadott számú szóval:

`crunch {{1}} {{5}} -o {{START}} -c {{1000}} -z {{gzip|bzip2|lzma|7z}}`
