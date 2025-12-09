# zsh

> Z SHell, een Bash-compatibele commandoregel-interpreteerder.
> Zie ook: `bash`, `histexpand`.
> Meer informatie: <https://zsh.sourceforge.io/Doc/Release/Invocation.html#Invocation>.

- Start een interactieve shell sessie:

`zsh`

- Voer specifieke [c]ommando's uit:

`zsh -c "{{echo Hello world}}"`

- Voer een specifiek script uit:

`zsh {{pad/naar/script.zsh}}`

- Controleer een specifiek script op syntax fouten zonder het uit te voeren:

`zsh --no-exec {{pad/naar/script.zsh}}`

- Voer specifieke commando's uit van `stdin`:

`{{echo Hello world}} | zsh`

- Voer een specifiek script uit en toon elke opdracht in het script voordat deze wordt uitgevoerd:

`zsh --xtrace {{pad/naar/script.zsh}}`

- Start een interactieve shell sessie in verbose modus en toon elke opdracht voordat deze wordt uitgevoerd:

`zsh --verbose`

- Voer een specifiek commando uit binnen `zsh` met uitgeschakelde glob patronen:

`noglob {{commando}}`
