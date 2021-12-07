# vim

> Vim (Vi IMproved), ein Befehlszeilen-Texteditor, bietet mehrere Modi für verschiedene Arten der Textmanipulation an.
> Das Drücken von `i` schaltet den Editier-Modus ein. `<Esc>` wechselt in den Befehls-Modus, der die Verwendung von Vim-Befehlen ermöglicht.
> Weitere Informationen: <https://www.vim.org>.

- Öffne eine Datei:

`vim {{pfad/zu/datei}}`

- Öffne eine Datei an einer bestimmten Zeilennummer:

`vim +{{zeilennummer}} {{pfad/zu/datei}}`

- Zeige Vim's Benutzeranleitung:

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
