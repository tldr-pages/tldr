# tput

> Vizualizaţi şi modificaţi setările şi capacităţile terminalelor.

- Mutați cursorul într-o locație de ecran:

`tput cup {{y_coordinate}} {{x_coordinate}}`

- Setați culoarea planului frontal (af) sau fundal (ab):

`tput {{setaf|setab}} {{ansi_color_code}}`

- Afișează numărul de coloane, linii sau culori:

`tput {{cols|lines|colors}}`

- Sună clopoţelul terminalului:

`tput bel`

- Resetați toate atributele terminalului

`tput sgr0`

- Activați/Dezactivați înfășurarea cuvintelor:

`tput {{smam|rmam}}`
