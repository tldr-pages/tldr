# renice

> Módosítja egy vagy több futó folyamat ütemezési prioritását/népszerűségét. Az értékek -20 (a folyamat számára legkedvezőbb) és 19 (a folyamat számára legkedvezőtlenebb) között mozognak. További információ: <https://manned.org/renice>.

- Egy futó folyamat prioritásának módosítása:

`renice -n {{niceness_value}} -p {{pid}}`

- A felhasználó tulajdonában lévő összes folyamat prioritásának módosítása:

`renice -n {{niceness_value}} -u {{user}}`

- Egy folyamatcsoporthoz tartozó összes folyamat prioritásának módosítása:

`renice -n {{niceness_value}} --pgrp {{process_group}}`
