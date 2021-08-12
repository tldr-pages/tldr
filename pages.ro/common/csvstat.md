# csvstat

> Imprimați statistici descriptive pentru toate coloanele dintr-un fișier CSV.
> Inclus în csvkit.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>

- Afișează toate statisticile pentru toate coloanele:

`csvstat {{data.csv}}`

- Afișează toate statisticile pentru coloanele 2 și 4:

`csvstat -c {{2,4}} {{data.csv}}`

- Afișează sumele pentru toate coloanele:

`csvstat --sum {{data.csv}}`

- Afișează lungimea valorii maxime pentru coloana 3:

`csvstat -c {{3}} --len {{data.csv}}`

- Afișați numărul de valori unice în coloana „nume”:

`csvstat -c {{name}} --unique {{data.csv}}`
