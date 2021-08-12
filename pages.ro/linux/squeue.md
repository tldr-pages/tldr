# squeue

> Vizualizaţi activităţile aflate în coada de aşteptare în programatorul SLURM.

- Vezi coada de așteptare:

`squeue`

- Vezi locuri de muncă în coadă de un anumit utilizator:

`squeue -u {{username}}`

- Vizualizați coada de așteptare și reîmprospătați la fiecare 5 secunde:

`squeue -i {{5}}`

- Vizualizați coada de așteptare cu timpii de începere așteptați:

`squeue --start`
