# renice

> Alterează prioritatea/amagiile de programare ale unuia sau mai multor procese care rulează.
> Valorile de bunătate variază de la -20 (cel mai favorabil procesului) la 19 (cel mai puțin favorabil procesului).

- Modificarea priorității unui proces în curs de desfășurare:

`renice -n {{niceness_value}} -p {{pid}}`

- Schimbarea priorității tuturor proceselor deținute de un utilizator:

`renice -n {{niceness_value}} -u {{user}}`

- Schimbarea priorității tuturor proceselor care aparțin unui grup de proces:

`renice -n {{niceness_value}} --pgrp {{process_group}}`
