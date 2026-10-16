# chgrp

> Verander de eigenaarsgroep van bestanden en mappen.
> Zie ook: `chown`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>.

- Verander de eigenaarsgroep van een bestand of map:

`chgrp {{groep}} {{pad/naar/bestand_of_map}}`

- Verander recursief de eigenaarsgroep van een map en alle bestanden erin:

`chgrp {{[-R|--recursive]}} {{groep}} {{pad/naar/map}}`

- Verander de eigenaarsgroep van een symbolische link:

`chgrp {{[-h|--no-dereference]}} {{groep}} {{pad/naar/symlink}}`

- Verander de eigenaarsgroep van een bestand/map naar dezelfde als een referentiebestand:

`chgrp --reference {{pad/naar/referentiebestand}} {{pad/naar/bestand_of_map}}`
