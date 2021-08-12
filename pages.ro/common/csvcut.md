# csvcut

> Filtrarea şi trunchierea fişierelor CSV. Cum ar fi comanda 'cut' a lui Unix, dar pentru date tabelare.
> Inclus în csvkit.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>

- Imprimați indicii și numele tuturor coloanelor:

`csvcut -n {{data.csv}}`

- Extrageţi prima şi a treia coloană:

`csvcut -c {{1,3}} {{data.csv}}`

- Extrageţi toate coloanele **cu excepţia celei de-a patra:

`csvcut -C {{4}} {{data.csv}}`

- Extrageţi coloanele denumite „id” şi „prenume” (în această ordine):

`csvcut -c {{id,"first name"}} {{data.csv}}`
