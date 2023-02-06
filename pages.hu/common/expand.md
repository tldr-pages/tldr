# expand

> A tabulátorokat szóközökké alakítja. További információ: <https://www.gnu.org/software/coreutils/expand>.

- A tabulátorokat minden fájlban szóközökké alakítja, a szabványos kimenetre írva:

`expand {{path/to/file}}`

- A tabulátorok szóközökké alakítása, olvasás a standard bemenetről:

`expand`

- Ne alakítsa át a tabulátorokat a nem üres részek után:

`expand -i {{path/to/file}}`

- A tabulátorok egymástól bizonyos számú karakterre legyenek, nem 8-ra:

`expand -t={{number}} {{path/to/file}}`

- Használjon vesszővel elválasztott listát az explicit tabulátorpozíciókról:

`expand -t={{1,4,6}}`
