# mkfile

> Egy vagy több, tetszőleges méretű üres fájl létrehozása. További információ: <https://manned.org/mkfile>.

- Hozzon létre egy 15 kilobájtos üres fájlt:

`mkfile -n {{15k}} {{path/to/file}}`

- Adott méretű és egységű (byte, KB, MB, GB) fájl létrehozása:

`mkfile -n {{size}}{{b|k|m|g}} {{path/to/file}}`

- Két, egyenként 4 megabájtos fájl létrehozása:

`mkfile -n {{4m}} {{first_filename}} {{second_filename}}`
