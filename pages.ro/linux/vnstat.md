# vnstat

> Un monitor de trafic de rețea bazat pe consolă.

- Afișează rezumatul traficului pentru toate interfețele:

`vnstat`

- Afișează rezumatul traficului pentru o anumită interfață de rețea:

`vnstat -i {{eth0}}`

- Afișează statistici live pentru o anumită interfață de rețea:

`vnstat -l -i {{eth0}}`

- Afișați statisticile de trafic pe o bază orară în ultimele 24 de ore folosind un grafic cu bare:

`vnstat -hg`

- Măsurați și afișați traficul mediu timp de 30 de secunde:

`vnstat -tr {{30}}`
