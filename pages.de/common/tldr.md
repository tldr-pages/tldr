# tldr

> Zeigt kurze Zusammenfassungen (tldr-Seiten) von Kommandozeilen-Befehlen an.
> Weitere Informationen: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Zeige die tldr-Seite für einen Befehl an (Hinweis: So bist du hierher gekommen!):

`tldr {{befehl}}`

- Zeige die tldr-Seite für `cd` an und überschreibe die Standardplattform:

`tldr -p {{android|linux|osx|sunos|windows}} {{cd}}`

- Zeige die tldr-Seite für einen Unterbefehl:

`tldr {{git-checkout}}`

- Aktualisiere die lokalen Seiten (wenn er Client Caching unterstützt):

`tldr -u`
