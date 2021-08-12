# mpstat

> Raportați statisticile procesorului.

- Afișează statistici CPU la fiecare 2 secunde:

`mpstat {{2}}`

- Afișează 5 rapoarte, unul câte unul, la intervale de 2 secunde:

`mpstat {{2}} {{5}}`

- Afișează 5 rapoarte, unul câte unul, de la un procesor dat, la intervale de 2 secunde:

`mpstat -P {{0}} {{2}} {{5}}`
