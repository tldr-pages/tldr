# basenc

> Encodeer of decodeer een bestand of `stdin` door gebruik te maken van een specifieke encoding naar `stdout`.
> Meer informatie: <https://www.gnu.org/software/coreutils/basenc>.

- Encodeer een bestand met base64 encoding:

`basenc --base64 {{pad/naar/bestand}}`

- Decodeer een bestand met base64 encoding:

`basenc --decode --base64 {{pad/naar/bestand}}`

- Encodeer `stdin` met base32 encoding met 42 kolommen:

`{{command}} | basenc --base32 -w42`

- Encodeer `stdin` met base32 encoding:

`{{command}} | basenc --base32`
