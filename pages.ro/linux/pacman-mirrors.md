# pacman-mirrors

> Generați o listă de oglinzi Pacman pentru Manjaro Linux.
> Fiecare rulare de pacman-oglinzi necesită sincronizarea bazei de date și actualizarea sistemului folosind `sudo pacman -Syyu`.
> Mai multe informaţii: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>

- Generați o listă de oglinzi utilizând setările implicite:

`sudo pacman-mirrors --fasttrack`

- Obțineți starea oglinzilor curente:

`pacman-mirrors --status`

- Afișează ramura curentă:

`pacman-mirrors --get-branch`

- Treceți la o ramură diferită:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Generați o listă de oglinzi, folosind doar oglinzi în țara dvs.:

`sudo pacman-mirrors --geoip`
