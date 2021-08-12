# stress

> Un instrument de testare a stresului CPU, memorie și IO pe un sistem Linux.

- Spawn 4 lucrători la stres test CPU:

`stress -c {{4}}`

- Spawn 2 lucrători la testul de stres IO și timeout după 5 secunde:

`stress -i {{2}} -t {{5}}`

- Spawn 2 lucrători la memorie test de stres (fiecare lucrător alocă 256M octeţi):

`stress -m {{2}} --vm-bytes {{256M}}`

- Spawn 2 lucrători filare pe scriere () /unlink () (fiecare lucrător scrie 1G octeți):

`stress -d {{2}} --hdd-bytes {{1GB}}`
