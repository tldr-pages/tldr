# enscript

> Conversia fişierelor text în PostScript, HTML, RTF, ANSI şi overstrikes.
> Mai multe informaţii: <https://www.gnu.org/software/enscript>

- Generarea unui fişier PostScript dintr-un fişier text:

`enscript {{path/to/input_file}} --output={{path/to/output_file}}`

- Generarea unui fişier într-o altă limbă decât PostScript:

`enscript {{path/to/input_file}} --language={{html|rtf|...}} --output={{path/to/output_file}}`

- Generați un fișier PostScript cu un aspect peisaj, împărțind pagina în coloane (maxim 9):

`enscript {{path/to/input_file}} --columns={{num}} --landscape --output={{path/to/output_file}}`

- Afișează sintaxa disponibilă evidențierea limbilor și formatelor de fișiere:

`enscript --help-highlight`

- Generați un fișier PostScript cu evidențierea sintaxei și culoarea pentru o limbă specificată:

`enscript {{path/to/input_file}} --color=1 --highlight={{language}} --output={{path/to/output_file}}`
