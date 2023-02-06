# trans

> A Translate Shell egy parancssori fordító. További információ: <https://github.com/soimort/translate-shell>.

- Fordítson le egy szót (a nyelv automatikusan felismerésre kerül):

`trans "{{word_or_sentence_to_translate}}"`

- Rövid fordítás lekérése:

`trans --brief "{{word_or_sentence_to_translate}}"`

- Fordítson le egy szót franciára:

`trans :{{fr}} {{word}}`

- Fordítson le egy szót németről angolra:

`trans {{de}}:{{en}} {{Schmetterling}}`

- Viselkedjen úgy, mint egy szótár, hogy megtudja egy szó jelentését:

`trans -d {{word}}`
