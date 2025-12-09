# wc

> Tel regels, woorden of bytes.
> Meer informatie: <https://keith.github.io/xcode-man-pages/wc.1.html>.

- Tel regels in een bestand:

`wc -l {{pad/naar/bestand}}`

- Tel woorden in een bestand:

`wc -w {{pad/naar/bestand}}`

- Tel tekens (bytes) in een bestand:

`wc -c {{pad/naar/bestand}}`

- Tel tekens in een bestand (rekening houdend met multi-byte tekensets):

`wc -m {{pad/naar/bestand}}`

- Gebruik `stdin` om regels, woorden en tekens (bytes) in die volgorde te tellen:

`{{find .}} | wc`
