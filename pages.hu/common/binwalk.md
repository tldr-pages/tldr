# binwalk

> Firmware Analysis Tool. További információ: <https://github.com/ReFirmLabs/binwalk>.

- Bináris fájl beolvasása:

`binwalk {{path/to/binary}}`

- Fájlok kivonása bináris állományból a kimeneti könyvtár megadásával:

`binwalk --extract --directory {{output_directory}} {{path/to/binary}}`

- Fájlok rekurzív kivonása bináris állományból, a rekurziós mélység 2-re történő korlátozásával:

`binwalk --extract --matryoshka --depth {{2}} {{path/to/binary}}`

- Fájlok kivonása bináris állományból a megadott fájlaláírással:

`binwalk --dd '{{png image:png}}' {{path/to/binary}}`

- Egy bináris állomány entrópiájának elemzése, a diagram mentése a bináris állomány nevével megegyező névvel és a `.png` kiterjesztéssel:

`binwalk --entropy --save {{path/to/binary}}`

- Az entrópia, az aláírás és az opkódok elemzésének kombinálása egyetlen parancsban:

`binwalk --entropy --signature --opcodes {{path/to/binary}}`
