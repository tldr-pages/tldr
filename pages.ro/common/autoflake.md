# autoflake

> Un instrument pentru a elimina importurile și variabilele neutilizate din codul Python.
> Mai multe informaţii: <https://github.com/myint/autoflake>

- Eliminați variabilele neutilizate dintr-un singur fișier și afișați diff:

`autoflake --remove-unused-variables {{file.py}}`

- Eliminați importurile neutilizate din mai multe fișiere și afișați diffs:

`autoflake --remove-all-unused-imports {{file1.py}} {{file2.py}} {{file3.py}}`

- Eliminați variabilele neutilizate dintr-un fișier, suprascrierea fișierului:

`autoflake --remove-unused-variables --in-place {{file.py}}`

- Eliminați variabilele neutilizate recursiv din toate fișierele dintr-un director, suprascrierea fiecărui fișier:

`autoflake --remove-unused-variables --in-place --recursive {{path/to/directory}}`
