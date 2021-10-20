# vim
> Vim (Vi IMproved), ein Commandline Texteditor, bietet mehrere Modi für verschiedene Arten der Textmanipulation.
>
> Das Drücken von `i` schaltet in den Editier-Modus. `<Esc>` wechselt in den Befehls-Modus, der die Verwendung von Vim-Befehlen ermöglicht.
>
> Mehr Informationen: <https://www.vim.org>.

- Eine Datei öffnen:

`vim {{pfad/zur/datei}}`

- Speichern und Schließen:

`:wq<Enter>`

- Ich habe mich verrannt und will ohne Speichern einfach nur raus:

`<Esc>:q!`

- Suche nach einem Muster in der Datei (per `n`/`N` zum nächsten/vorherigen Treffer gehen):

`/{{suchmuster}}<Enter>`

- Per RegEx einen Begriff suchen/ersetzen - jeder Treffer wird ersetzt:

`:%s/{{regular_expression}}/{{neuer_text}}/g<Enter>`

- Die letzte Aktion rückgängig machen:

`u`
