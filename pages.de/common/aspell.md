# aspell

> Interaktiver Korrekturleser.
> Weitere Informationen: <http://aspell.net/man-html/index.html>.

- Überprüfe eine einzelne Datei auf Fehler:

`aspell check {{pfad/zu/datei}}`

- Liste falsch geschriebene Worte von `stdin`:

`cat {{pfad/zu/datei}} | aspell list`

- Zeige verfügbare Wörterbuchsprachen:

`aspell dicts`

- Nutze `aspell` mit einem anderen Wörterbuch (nimmt 2-Zeichen-Locale laut ISO 639 Sprach Code):

`aspell --lang {{cs}}`

- Zeige alle falsch geschriebenen Wörter von `stdin` und ignoriere alle Wörter in einer persönlichen Wortliste:

`cat {{pfad/zu/datei}} | aspell --personal {{persönliche-wort-liste.pws}} list`
