# join

> Asociați linii de două fișiere sortate într-un câmp comun.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/join>

- Alăturați-vă două fișiere pe primul câmp (implicit):

`join {{file1}} {{file2}}`

- Alăturați-vă două fișiere utilizând o virgulă (în loc de un spațiu) ca separator de câmp:

`join -t {{','}} {{file1}} {{file2}}`

- Alăturați-vă câmpul3 din fișier1 cu câmpul1 din fișier2:

`join -1 {{3}} -2 {{1}} {{file1}} {{file2}}`

- Produceți o linie pentru fiecare linie neperechabilă pentru fișier1:

`join -a {{1}} {{file1}} {{file2}}`
