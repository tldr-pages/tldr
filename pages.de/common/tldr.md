# tldr

> Zeigt kurze Zusammenfassungen (tldr-Seiten) von Kommandozeilen-Befehlen an.
> Weitere Informationen: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Zeige die tldr-Seite für einen Befehl an:

`tldr {{befehl}}`

- Zeige die tldr-Seite für einen Unterbefehl an:

`tldr {{befehl}} {{unterbefehl}}`

- Zeige die tldr-Seite für einen Befehl in einer bestimmten Sprache an (Hinweis: So bist du hierher gekommen!):

`tldr {{[-L|--language]}} {{sprachcode}} {{befehl}}`

- Zeige die tldr-Seite für einen Befehl auf einer bestimmten Plattform an:

`tldr {{[-p|--platform]}} {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{befehl}}`

- Aktualisiere den lokalen Cache:

`tldr {{[-u|--update]}}`

- Liste alle Seiten für die aktuelle Plattform und `common` auf:

`tldr {{[-l|--list]}}`

- Liste alle Unterbefehl-Seiten für einen Befehl auf:

`tldr {{[-l|--list]}} | grep {{befehl}} | column`

- Zeige die tldr-Seite für einen zufälligen Befehl an:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
