# yay

> Yet Another Yogurt: Ein Programm für Arch Linux um Pakete vom Arch User Repository zu installieren.
> Siehe auch `pacman`.
> Weitere Informationen: <https://github.com/Jguer/yay>.

- Suche und installiere Pakete von den Repositorys und dem AUR interaktiv:

`yay {{paketname|suchbegriff}}`

- Synchronisiere und aktualisiere alle Pakete von den Repositorys und dem AUR:

`yay`

- Synchronisiere und aktualisiere nur AUR-Pakete:

`yay -Sua`

- Installiere ein neues Paket von den Repositorys und dem AUR:

`yay -S {{paketname}}`

- Entferne ein Paket sowie alle Abhängigkeiten und Konfigurationsdateien:

`yay -Rns {{paketname}}`

- Suche in der Paketdatenbank nach einem Schlüsselwort in den Repositorys und dem AUR:

`yay -Ss {{schlüsselwort}}`

- Entferne verwaiste Pakete (als Abhängigkeit installiert, aber von keinem Paket benötigt):

`yay -Yc`

- Zeige Statistiken für installierte Pakete sowie die Gesundheit des Systems an:

`yay -Ps`
