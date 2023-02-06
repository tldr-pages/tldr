# base64

> Kódolás és dekódolás Base64 reprezentációval. További információ: <https://www.unix.com/man-page/osx/1/base64/>.

- Egy fájl kódolása:

`base64 --input={{plain_file}}`

- Egy fájl dekódolása:

`base64 --decode --input={{base64_file}}`

- Enkódolás a `stdin` oldalról:

`echo -n "{{plain_text}}" | base64`

- Dekódolás a `stdin`:

`echo -n {{base64_text}} | base64 --decode`
