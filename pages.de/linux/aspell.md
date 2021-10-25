# aspell

> Interaktiver Korrekturleser.
> Mehr Informationen: <http://aspell.net/>.

- Überprüfe eine einzelne Datei auf Fehler:

`aspell check {{pfad/zur/datei}}`

- Liste falsch geschriebene Worte von Standard Input:

`cat {{file}} | aspell list`

- Zeige verfügbare Wörterbücher Sprachen:

`aspell dicts`

- Nutze aspell mit einem anderen Wörterbuch (nimmt 2-Buchstaben-Sprachkürzel laut ISO 639 Sprach Code):

`aspell --lang={{cs}}`

- Zeige alle falsch geschriebenen Wörter von Standard Input und ignoriere alle Wörter in einer persönlichen Wortliste:

`cat {{file}} | aspell --personal={{persönliche-wort-liste.pws}} {{list}}`
