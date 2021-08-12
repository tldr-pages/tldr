# phing

> Un instrument de construire PHP bazat pe Apache Ant.
> Mai multe informaţii: <https://www.phing.info>

- Efectuați sarcina implicită în fișierul `build.xml`:

`phing`

- Inițializarea unui nou fișier de compilare:

`phing -i {{path/to/build.xml}}`

- Efectuați o anumită sarcină:

`phing {{task_name}}`

- Specificați o cale de fișier de compilare particularizată:

`phing -f {{path/to/build.xml}} {{task_name}}`

- Specificați un fișier jurnal pentru a ieși la:

`phing -b {{path/to/log_file}} {{task_name}}`

- Specificați proprietățile particularizate de utilizat în compilare:

`phing -D{{property}}={{value}} {{task_name}}`

- Specificați o clasă de ascultare personalizată:

`phing -listener {{class_name}} {{task_name}}`

- Construiți folosind ieșire verbose:

`phing -verbose {{task_name}}`
