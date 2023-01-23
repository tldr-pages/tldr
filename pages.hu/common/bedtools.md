# bedtools

> A genomikai elemzési feladatokhoz szükséges eszközök svájci bicskája. BAM, BED, GFF/GTF, VCF formátumú adatok metszésére, csoportosítására, konvertálására és számolására szolgál. További információ: <https://bedtools.readthedocs.io>.

- Két fájl metszése a szekvenciák szálát illetően, és az eredmény mentése a megadott fájlba:

`bedtools intersect -a {{path/to/file_1}} -b {{path/to/file_2}} -s > {{path/to/output_file}}`

- Két fájl metszése bal külső csatlakozással, azaz minden egyes jellemzőt jelentsen a {{file_1}} fájlból és NULL, ha nincs átfedés a {{file_2}}} fájllal:

`bedtools intersect -a {{path/to/file_1}} -b {{path/to/file_2}} -lof > {{path/to/output_file}}`

- Hatékonyabb algoritmus használata két előreszortált fájl metszéséhez:

`bedtools intersect -a {{path/to/file_1}} -b {{path/to/file_2}} -sorted > {{path/to/output_file}}`

- A {{`path/to/file`}} fájl csoportosítása az első három és az ötödik oszlop alapján, és a hatodik oszlop összegzése összegzéssel:

`bedtools groupby -i {{path/to/file}} -c 1-3,5 -g 6 -o sum`

- A bam-formátumú fájl átalakítása bed-formátumúvá:

`bedtools bamtobed -i {{path/to/file}}.bam > {{path/to/file}}.bed`

- Keresse meg a {{file_1}}.bed fájlban található összes jellemzőhöz a legközelebbi jellemzőt a {{file_2}}.bed fájlban, és írja ki a távolságukat egy külön oszlopba (a bemeneti fájloknak rendezettnek kell lenniük):

`bedtools closest -a {{path/to/file_1}}.bed -b {{path/to/file_2}}.bed -d`
