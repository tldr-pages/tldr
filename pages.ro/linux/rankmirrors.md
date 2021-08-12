# rankmirrors

> Clasificați o listă de oglinzi Pacman după conectare și viteza de deschidere.
> Scrie noua listă de oglinzi la stdout.
> Mai multe informaţii: <https://wiki.archlinux.org/index.php/mirrors>

- Rang o listă oglindă:

`rankmirrors {{/etc/pacman.d/mirrorlist}}`

- Ieșire doar un anumit număr de servere de top clasament:

`rankmirrors -n {{number}} {{/etc/pacman.d/mirrorlist}}`

- Fiți verbose atunci când generați oglinda:

`rankmirrors -v {{/etc/pacman.d/mirrorlist}}`

- Testați doar o adresă URL specifică:

`rankmirrors --url {{url}}`

- Ieșiți numai timpii de răspuns în locul unei liste de oglinzi complete:

`rankmirrors --times {{/etc/pacman.d/mirrorlist}}`
