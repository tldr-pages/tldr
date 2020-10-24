# trans

> Translate Shell is a command-line translator.
> More information: <https://github.com/soimort/translate-shell>.

- Translate a word (language is detected automatically):

`trans "{{word_or_sentence_to_translate}}"`

- Get a brief translation:

`trans --brief "{{word_or_sentence_to_translate}}"`

- Translate a word into french:

`trans :{{fr}} {{word}}`

- Translate a word from German to English:

`trans {{de}}:{{en}} {{Schmetterling}}`

- Behave like a dictionary to get the meaning of a word:

`trans -d {{word}}`
