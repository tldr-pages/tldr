# enscript

> Szövegfájlok átalakítása PostScript, HTML, RTF, ANSI és overstrikes formátumba. További információ: <https://www.gnu.org/software/enscript>.

- PostScript fájl generálása szöveges fájlból:

`enscript {{path/to/input_file}} --output={{path/to/output_file}}`

- A PostScript-től eltérő nyelvű fájl generálása:

`enscript {{path/to/input_file}} --language={{html|rtf|...}} --output={{path/to/output_file}}`

- PostScript-fájl generálása fekvő formátumban, az oldalt oszlopokra osztva (legfeljebb 9):

`enscript {{path/to/input_file}} --columns={{num}} --landscape --output={{path/to/output_file}}`

- A rendelkezésre álló szintaxiskiemelő nyelvek és fájlformátumok megjelenítése:

`enscript --help-highlight`

- PostScript-fájl generálása egy megadott nyelvhez tartozó szintaxis-kiemeléssel és színnel:

`enscript {{path/to/input_file}} --color=1 --highlight={{language}} --output={{path/to/output_file}}`
