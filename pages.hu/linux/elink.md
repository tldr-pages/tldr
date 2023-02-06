# elink

> Előre kiszámított szomszédok keresése egy adatbázisban, vagy kapcsolódó rekordok keresése más adatbázisokban. A `edirect` csomag része. További információ: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- Keresés a pubmedben, majd kapcsolódó szekvenciák keresése:

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}" | elink -target nuccore`

- Nukleotid keresés, majd rokon biominták keresése:

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}" | elink -target biosample`
