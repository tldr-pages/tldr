# bedtools

> Un cuțit elvețian-armată de instrumente pentru sarcini de analiză genomică.
> Utilizat pentru a intersecta, grupa, converti și număra date în format BAM, BED, GFF/GTF, VCF.
> Mai multe informaţii: <https://bedtools.readthedocs.io/en/latest/>

- Intersectează două fișiere cu privire la componenta secvențelor și salvează rezultatul în {{`path/to/output_file`}}:

`bedtools intersect -a {{path/to/file_1}} -b {{path/to/file_2}} -s > {{path/to/output_file}}`

- Intersectează două fișiere cu o asociere externă la stânga, adică raportează fiecare entitate din {{file_1}} și NULL dacă nu se suprapun cu {{file_2}}:

`bedtools intersect -a {{path/to/file_1}} -b {{path/to/file_2}} -lof > {{path/to/output_file}}`

- Folosind algoritm mai eficient pentru a intersecta două fișiere pre-sortate:

`bedtools intersect -a {{path/to/file_1}} -b {{path/to/file_2}} -sorted > {{path/to/output_file}}`

- Fișier de grup {{`cale/la/file`}} bazat pe primele trei și a cincea coloană și rezumă a șasea coloană prin însumarea acesteia:

`bedtools groupby -i {{path/to/file}} -c 1-3,5 -g 6 -o sum`

- Conversia fișierului formatat bam-într-un pat formatat:

`bedtools bamtobed -i {{path/to/file}}.bam > {{path/to/file}}.bed`

- Găsiți pentru toate caracteristicile din {{file_1}} .bed cel mai apropiat din {{file_2}} .bed și scrieți distanța lor într-o coloană suplimentară (fișierele de intrare trebuie sortate):

`bedtools closest -a {{path/to/file_1}}.bed -b {{path/to/file_2}}.bed -d`
