# qsub

> Remite un script la sistemul de gestionare a cozii de așteptare CUPLY.

- Trimiteți un script cu setări implicite (depinde de setările de cuplu):

`qsub {{script.sh}}`

- Trimiteți un script cu o limită de execuție specificată pentru wallclock de 1 oră, 2 minute și 3 secunde:

`qsub -l walltime={{1}}:{{2}}:{{3}} {{script.sh}}`

- Trimiteți un script care este executat pe 2 noduri folosind 4 nuclee pe nod:

`qsub -l nodes={{2}}:ppn={{4}} {{script.sh}}`

- Trimiteți un script la o anumită coadă. Rețineți că cozile diferite pot avea limite maxime și minime de execuție diferite:

`qsub -q {{queue_name}} {{script.sh}}`
