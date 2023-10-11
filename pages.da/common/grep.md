# grep

> Find mønstre i filer via regulære udtryk (regular expressions).
> Mere information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Søg efter et mønster i en fil:

`grep "{{søgemønster}}" {{sti/til/fil}}`

- Søg efter en eksakt streng (deaktiverer regulære udtryk):

`grep --fixed-strings "{{eksakt_streng}}" {{sti/til/fil}}`

- Søg efter et mønster i alle filer, pånær binære, rekursivt i en mappe. Vis linjenumre der matcher til mønstret:

`grep --recursive --line-number --binary-files={{without-match}} "{{søgemønster}}" {{sti/til/mappe}}`

- Brug udvidede regulære udtryk (understøtter `?`, `+`, `{}`, `()` og `|`), i case-insensitive modus:

`grep --extended-regexp --ignore-case "{{søgemønster}}" {{sti/til/fil}}`

- Print 3 linjer af kontekst omkring, før eller efter hvert match:

`grep --{{context|before-context|after-context}}={{3}} "{{søgemønster}}" {{sti/til/fil}}`

- Print, filnavn og linjenummer for hvert match, med farveoutput:

`grep --with-filename --line-number --color=always "{{søgemønster}}" {{sti/til/fil}}`

- Søg efter linjer som matcher et mønster. Print kun den matchende tekst:

`grep --only-matching "{{søgemønster}}" {{sti/til/fil}}`

- Søg i `stdin` efter linjer der ikke matcher et mønster:

`cat {{sti/til/fil}} | grep --invert-match "{{søgemønster}}"`
