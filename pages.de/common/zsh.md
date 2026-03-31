# zsh

> Z SHell. Mit `bash` und `sh` kompatible Eingabeaufforderung.
> Siehe auch: `bash`, `!`, `^`.
> Weitere Informationen: <https://zsh.sourceforge.io/Doc/Release/Invocation.html#Invocation>.

- Starte eine interaktive Eingabeaufforderung:

`zsh`

- Führe Parameter als Befehl aus:

`zsh -c {{befehl}}`

- Führe Befehle aus einem Skript aus:

`zsh {{pfad/zu/skript}}`

- Prüfe ein Skript nach Syntaxfehlern, ohne es auszuführen:

`zsh {{[-n|--no-exec]}} {{pfad/zu/skript}}`

- Führe Befehle von `stdin` aus:

`{{echo echo Hello World}} | zsh`

- Führe Befehle aus einem Skript aus und schreibe die Befehle in die Konsole:

`zsh {{[-x|--xtrace]}} {{pfad/zu/skript}}`

- Starte eine interaktive Eingabeaufforderung, in der jeder Befehl ausgegeben wird, bevor er ausgeführt wird:

`zsh {{[-v|--verbose]}}`

- Starte Zsh, ohne Nutzerkonfigurationen zu laden (z.B. `~/.zshrc`):

`zsh {{[-f|--no-rcs]}}`
