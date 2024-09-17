# base64

> Encodeer en decodeer met behulp van Base64-representatie.
> Meer informatie: <https://keith.github.io/xcode-man-pages/base64.1.html>.

- Encodeer een bestand:

`base64 --input={{gewoon_bestand}}`

- Decodeer een bestand:

`base64 --decode --input={{base64_bestand}}`

- Encodeer vanaf `stdin`:

`echo -n "{{platte_tekst}}" | base64`

- Decodeer vanaf `stdin`:

`echo -n {{base64_tekst}} | base64 --decode`
