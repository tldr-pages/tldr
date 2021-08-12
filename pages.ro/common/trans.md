# trans

> Traducere shell este un traducător de linie de comandă.
> Mai multe informaţii: <https://github.com/soimort/translate-shell>

- Traduceți un cuvânt (limba este detectată automat):

`trans "{{word_or_sentence_to_translate}}"`

- Obțineți o scurtă traducere:

`trans --brief "{{word_or_sentence_to_translate}}"`

- Traduceți un cuvânt în franceză:

`trans :{{fr}} {{word}}`

- Traduceți un cuvânt din germană în engleză:

`trans {{de}}:{{en}} {{Schmetterling}}`

- Comportă-te ca un dicționar pentru a obține sensul unui cuvânt:

`trans -d {{word}}`
