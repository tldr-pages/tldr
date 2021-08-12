# sar

> Monitorizarea performanțelor diferitelor subsisteme Linux.

- Raportați I/O și rata de transfer emisă dispozitivelor fizice, o dată pe secundă (apăsați CTRL+C pentru a ieși):

`sar -b {{1}}`

- Raportați un total de 10 statistici ale dispozitivelor de rețea, una la 2 secunde:

`sar -n DEV {{2}} {{10}}`

- Raportați utilizarea procesorului, una la 2 secunde:

`sar -u ALL {{2}}`

- Raportați un total de 20 de statistici de utilizare a memoriei, una pe secundă:

`sar -r ALL {{1}} {{20}}`

- Raportați lungimea cozii de rulare și mediile de încărcare, una pe secundă:

`sar -q {{1}}`

- Raportați statistici de paginare, câte una la 5 secunde:

`sar -B {{5}}`
