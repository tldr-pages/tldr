# ugrep

> Ultraschnelles Suchtool mit Abfrage-UI.
> Weitere Informationen: <https://github.com/Genivia/ugrep>.

- Ausführen das interaktives Suchtool TUI (CTRL-Z um Hilfe):

`ugrep -Q`

- Suche rekursiv alle Dateien die ein reguläres Ausdrucksmuster enthalten:

`ugrep "{{SuchMuster}}"`

- Fallunabhängige Suche:

`ugrep -i "{{SuchMuster}}"`

- [L]iste der passenden Dateien:

`ugrep -l "{{SuchMuster}}"`

- Suche komprimierte Dateien, [z]ip- und tar-Archive:

`ugrep -z "{{SuchMuster}}"`

- Suche fu[z]zy reguläres Ausdrucksmuster mit maximal 3 zusätzliche, fehlende oder nicht übereinstimmende Zeichen:

`ugrep -Z3 "{{SuchMuster}}"`

- Suche nur Dateien deren Dateinamen mit einem [g]lob-Muster übereinstimmen:

`ugrep -g "{{GlobMuster}}" "{{SuchMuster}}"`

- Suche nur nach Dateien eines bestimmten [T]yps oder eines anderen Typs und nicht nach einem Typ

`ugrep -t {{Typ}},{{oder_Typ}},^{{night_Typ}} "{{SuchMuster}}"`
