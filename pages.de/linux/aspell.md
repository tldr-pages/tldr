# aspell

> Interaktiver Korrekturleser.
> Weitere Informationen: <http://aspell.net/>.

- Überprüfe eine einzelne Datei auf Fehler:

`aspell check {{pfad/zur/datei}}`

- Liste falsch geschriebene Worte von Standard Input:

`cat {{file}} | aspell list`

- Zeige verfügbare Wörterbuchsprachen:

`aspell dicts`

- Nutze `aspell` mit einem anderen Wörterbuch (nimmt 2-Zeichen-Locale laut ISO 639 Sprach Code):

`aspell --lang={{cs}}`

- Zeige alle falsch geschriebenen Wörter von Standard Input und ignoriere alle Wörter in einer persönlichen Wortliste:

`cat {{file}} | aspell --personal={{persönliche-wort-liste.pws}} list`
