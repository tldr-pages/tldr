# dvc gc

> Eliminați fișierele și directoarele neutilizate din memoria cache sau spațiul de stocare la distanță.
> Mai multe informaţii: <https://dvc.org/doc/command-reference/gc>

- Gunoi colecta din memoria cache, păstrând doar versiunile la care se face referire spațiul de lucru curent:

`dvc gc --workspace`

- Gunoiul se colectează din memoria cache, păstrând doar versiunile la care se face referire după sucursală, etichete și angajări:

`dvc gc --all-branches --all-tags --all-commits`

- Gunoi colecta din memoria cache, inclusiv spațiul implicit de stocare la distanță nor (dacă este setat):

`dvc gc --all-commits --cloud`

- Gunoiul se colectează din memoria cache, inclusiv o anumită stocare la distanță cloud:

`dvc gc --all-commits --cloud --remote {{remote_name}}`
