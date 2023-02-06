# esearch

> Új Entrez keresés végrehajtása az indexált mezőkben található kifejezések felhasználásával. A `edirect` csomag része. További információ: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Keressen a pubmed adatbázisban a szelektív szerotonin visszavétel gátlóra:

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}"`

- Keresés a fehérje adatbázisban egy lekérdezés és egy regexp segítségével:

`esearch -db {{protein}} -query {{'Escherichia*'}}`

- Keressen olyan szekvenciákat a nukleotidadatbázisban, amelyek metaadataiban inzulin és rágcsálók szerepelnek:

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}"`

- Megjelenítés \[h\]elp:

`esearch -h`
