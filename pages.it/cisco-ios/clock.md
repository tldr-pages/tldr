# clock

> Imposta l'orologio di sistema.
> Maggiori informazioni: <https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book/cf_c1.html#clock>.

- Entra in modalità esecuzione privilegiata:

`clock set {{23}}:{{59}}:{{59}} {{31}} {{april}} {{2000}}`

- Autonegozia con l'estremità lontana del collegamento, impostazione predefinita su active-clock:

`clock active prefer`

- Autonegozia con l'estremità lontana del collegamento, impostazione predefinita su passive-clock:

`clock passive prefer`

- Mostra la modalità clock corrente negoziata dal firmware:

`clock show interfaces`
