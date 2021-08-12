# quotacheck

> Scanați un sistem de fișiere pentru utilizarea discului; creați, verificați și reparați fișiere de cote.
> Cel mai bine este să rulați verificarea cotelor cu cotele dezactivate pentru a preveni deteriorarea sau pierderea fișierelor de cotă.

- Verificați cotele pentru toate sistemele de fișiere non-NFS montate:

`sudo quotacheck --all`

- Verificarea forței, chiar dacă cotele sunt activate (acest lucru poate cauza deteriorarea sau pierderea fișierelor de cote):

`sudo quotacheck --force {{mountpoint}}`

- Verificați cotele pe un anumit sistem de fișiere în modul de depanare:

`sudo quotacheck --debug {{mountpoint}}`

- Verificați cotele pe un anumit sistem de fișiere, afișând progresul:

`sudo quotacheck --verbose {{mountpoint}}`

- Verificați cotele utilizatorilor:

`sudo quotacheck --user {{user}} {{mountpoint}}`

- Verificați cotele de grup:

`sudo quotacheck --group {{group}} {{mountpoint}}`
