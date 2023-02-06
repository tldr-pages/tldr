# einfo

> Megadja az adott adatbázis egyes mezőiben indexált rekordok számát, az adatbázis utolsó frissítésének dátumát, valamint az adatbázisból más Entrez-adatbázisokhoz elérhető linkeket. További információ: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Az összes adatbázis nevének kiírása:

`einfo -dbs`

- A fehérjeadatbázis összes információjának kinyomtatása XML formátumban:

`einfo -db {{protein}}`

- A nuccore adatbázis összes mezőjének nyomtatása:

`einfo -db {{nuccore}} -fields`

- A fehérjeadatbázis összes linkjének kinyomtatása:

`einfo -db {{protein}} -links`
