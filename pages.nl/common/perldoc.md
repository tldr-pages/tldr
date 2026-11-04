# perldoc

> Zoek Perl-documentatie op in `.pod`-formaat.
> Meer informatie: <https://perldoc.perl.org/perldoc>.

- Bekijk documentatie voor een ingebouwde [f]unctie, een [v]ariabele of een [a]PI:

`perldoc -{{f|v|a}} {{naam}}`

- Zoek in de [q]uestion-koppen van de Perl FAQ:

`perldoc -q {{regex}}`

- Stuur de uitvoer direct naar `stdout` (standaard wordt het naar een pager gestuurd):

`perldoc -T {{pagina|module|programma|url}}`

- Specificeer de taalcode van de gewenste vertaling:

`perldoc -L {{taalcode}} {{pagina|module|programma|url}}`
