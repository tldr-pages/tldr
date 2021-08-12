# expr

> Evaluați expresiile și manipulați șiruri de caractere.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/expr>

- Ia lungimea șirului:

`expr length {{string}}`

- Evaluați expresia logică sau matematică cu un operator ('+', '-', '*', '&', '|' etc.). Simbolurile speciale ar trebui să fie scăpat:

`expr {{first_argument}} {{operator}} {{second_argument}}`

- Obțineți poziția primului caracter din „string” care se potrivește cu „substring”:

`echo $(expr index {{string}} {{substring}})`

- Extrage o parte din șir:

`echo $(expr substr {{string}} {{position_to_start}} {{number_of_characters}}`

- Extrage o parte a șirului care se potrivește cu o expresie regulată:

`echo $(expr {{string}} : '\({{regular_expression}}\)')`
