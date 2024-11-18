# argos-translate

> An Open-source offline translation library and CLI tool written in Python.
> More information: <https://www.argosopentech.com/>.

- Install translation pairs for Spanish to English translation:

`argospm install translate-es_en`

- Translate some text from Spanish (es) to English (en) (Note: only two letter language codes are supported):

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- Translate a text file from English to Hindi:

`cat {{path/to/file.txt}} | argos-translate --from-lang en --to-lang hi`

- List all installed translation pairs:

`argospm list`

- Show translation pairs from English available to be installed:

`argospm search --from-lang en`

- Update installed language package pairs:

`argospm update`

- Translate from `ar` to `ru`. When the translation pairs `translate-es_en` and `translate-en_ru` are installed:

`argos-translate --from-lang es --to-lang ru {{una imagen vale más que mil palabras}}`
