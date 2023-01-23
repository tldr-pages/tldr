# lrunzip

> Nagyméretű fájlok dekompressziós programja. Lásd még: `lrzip`, `lrztar`, `lrzuntar`. További információ: <https://manned.org/lrunzip>.

- Egy fájl dekompressziója:

`lrunzip {{filename.lrz}}`

- Egy fájl dekompressziója meghatározott számú processzorszál felhasználásával:

`lrunzip -p {{8}} {{filename.lrz}}`

- Egy fájl dekompressziója és a fájlok csendes felülírása, ha léteznek:

`lrunzip -f {{filename.lrz}}`

- Törött vagy sérült fájlok megtartása ahelyett, hogy a dekompresszáláskor törölné őket:

`lrunzip -K {{filename.lrz}}`

- Kimeneti fájlnév és/vagy elérési útvonal megadása:

`lrunzip -o {{outfilename}} {{filename.lrz}}`
