# vi

> Dieser Befehl ist ein Alias von `vim`.

- Zeige die Dokumentation für den originalen Befehl an:

`tldr vim`

- Öffne eine Datei:

`vi {{pfad/zu/datei}}`

- Öffne eine Datei an einer bestimmten Zeilennummer:

`vi +{{zeilennummer}} {{pfad/zu/datei}}`

- Zeige Vi's Benutzeranleitung:

`:help<Enter>`

- Speichere und schließe die aktuelle Datei:

`:wq<Enter>`

- Mache die letzte Aktion rückgängig:

`u`

- Suche nach einem Muster in der Datei (mit `n`/`N` zum nächsten/vorherigen Treffer gehen):

`/{{suchmuster}}<Enter>`

- Ersetze einen regulären Ausdruck alle Treffer in einer Datei:

`:%s/{{regulärer_ausdruck}}/{{neuer_text}}/g<Enter>`

- Zeige Zeilennummern an:

`:set nu<Enter>`
