# pygmentize

> Python-alapú szintaxis kiemelő. További információ: <https://pygments.org/docs/cmdline/>.

- Kiemeli a fájl szintaxisát és kiírja a standard kimenetre (a nyelvre a fájl kiterjesztéséből következtet):

`pygmentize {{file.py}}`

- A szintaxis kiemelés nyelvének explicit beállítása:

`pygmentize -l {{javascript}} {{input_file}}`

- A rendelkezésre álló lexerek (a bemeneti nyelvek feldolgozói) listája:

`pygmentize -L lexers`

- A kimenet mentése HTML formátumú fájlba:

`pygmentize -f html -o {{output_file.html}} {{input_file.py}}`

- A rendelkezésre álló kimeneti formátumok listája:

`pygmentize -L formatters`

- HTML-fájl kimenete, további formázási beállításokkal (teljes oldal, sorszámozással):

`pygmentize -f html -O "full,linenos=True" -o {{output_file.html}} {{input_file}}`
