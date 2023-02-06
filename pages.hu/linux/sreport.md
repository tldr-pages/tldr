# sreport

> Jelentések készítése a munkákról, felhasználókról és fürtökről a könyvelési adatokból. További információ: <https://slurm.schedmd.com/sreport.html>.

- Pipával elválasztott fürthasználati adatok megjelenítése:

`sreport --parsable cluster utilization`

- A lefuttatott munkák számának megjelenítése:

`sreport job sizes printjobcount`

- A legnagyobb CPU-időfelhasználású felhasználók megjelenítése:

`sreport user topuser`
