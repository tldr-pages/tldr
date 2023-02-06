# qsub

> Szkriptet küld a TORQUE várólista-kezelő rendszerbe. További információ: <https://manned.org/qsub.1>.

- Szkript elküldése alapértelmezett beállításokkal (a TORQUE beállításaitól függ):

`qsub {{script.sh}}`

- Szkript elküldése 1 óra, 2 perc és 3 másodperces megadott falióra-futási időhatárral:

`qsub -l walltime={{1}}:{{2}}:{{3}} {{script.sh}}`

- Küldjön be egy olyan szkriptet, amely 2 csomóponton, csomópontonként 4 magot használva kerül végrehajtásra:

`qsub -l nodes={{2}}:ppn={{4}} {{script.sh}}`

- Szkript benyújtása egy adott várólistára. Vegye figyelembe, hogy a különböző várólisták eltérő maximális és minimális futási időkorlátokkal rendelkezhetnek:

`qsub -q {{queue_name}} {{script.sh}}`
