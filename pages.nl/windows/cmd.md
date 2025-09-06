# cmd

> De Windows-opdrachtinterpreter.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Start een interactieve shell-sessie:

`cmd`

- Voer specifieke [c]ommandos uit:

`cmd /c {{echo Hello world}}`

- Voer een specifiek script uit:

`cmd {{pad\naar\script.bat}}`

- Voer specifieke commando's uit en start vervolgens een interactieve shell:

`cmd /k {{echo Hello world}}`

- Start een interactieve shell-sessie waarbij `echo` is uitgeschakeld in de opdrachtuitvoer:

`cmd /q`

- Start een interactieve shell-sessie met vertraagde [v]ariabele-expansie in- of uitgeschakeld:

`cmd /v:{{on|off}}`

- Start een interactieve shell-sessie met opdracht[e]xtensies in- of uitgeschakeld:

`cmd /e:{{on|off}}`

- Start een interactieve shell-sessie met gebruikte [u]nicode-codering:

`cmd /u`
