# basenc

> Encodeer of decodeer een bestand of `stdin` door gebruik te maken van een specifieke encoding naar `stdout`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>.

- Encodeer een bestand met base64 encoding:

`basenc --base64 {{pad/naar/bestand}}`

- Decodeer een bestand met base64 encoding:

`basenc {{[-d|--decode]}} --base64 {{pad/naar/bestand}}`

- Encodeer `stdin` met base32 encoding met 42 kolommen:

`{{commando}} | basenc --base32 {{[-w|--wrap]}} 42`

- Encodeer `stdin` met base32 encoding:

`{{commando}} | basenc --base32`
