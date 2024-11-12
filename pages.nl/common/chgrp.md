# chgrp

> Verander beheerdersgroep van bestanden en mappen.
> Meer informatie: <https://www.gnu.org/software/coreutils/chgrp>.

- Verander beheerdergroep van een bestand of map:

`chgrp {{groep}} {{pad/naar/bestand_of_map}}`

- Verander recursief de beheerdersgroep van een map en alle bestanden erin:

`chgrp -R {{groep}} {{pad/naar/map}}`

- Verander beheerdersgroep van een symbolische link:

`chgrp -h {{groep}} {{pad/naar/symlink}}`

- Verander de beheerdersgroep van een bestand/map naar de permissies van een referentiebestand:

`chgrp --reference {{pad/naar/referentiebestand}} {{pad/naar/bestand_of_map}}`
