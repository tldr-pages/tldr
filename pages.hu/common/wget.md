# wget

> Letöltés a webről, HTTP, HTTPS és FTP támogatással. További információ: <https://www.gnu.org/software/wget>.

- Letölti egy URL tartalmát egy fájlba (ebben az esetben "foo" néven):

`wget {{https://example.com/foo}}`

- Egy URL tartalmának letöltése egy fájlba (ebben az esetben "bar" néven):

`wget --output-document {{bar}} {{https://example.com/foo}}`

- Egyetlen weboldal és annak összes erőforrása letöltése 3 másodperces időközökkel a kérések között (szkriptek, stílustáblák, képek stb.):

`wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}}`

- Egy könyvtárban és annak alkönyvtáraiban található összes felsorolt fájl letöltése (a beágyazott oldalelemeket nem tölti le):

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- Korlátozza a letöltési sebességet és a kapcsolat újrapróbálkozásainak számát:

`wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- Fájl letöltése HTTP-kiszolgálóról Basic Auth használatával (FTP esetén is működik):

`wget --user={{username}} --password={{password}} {{https://example.com}}`

- Folytathatja a befejezetlen letöltést:

`wget --continue {{https://example.com}}`

- Egy szöveges fájlban tárolt összes URL letöltése egy adott könyvtárba:

`wget --directory-prefix {{path/to/directory}} --input-file {{URLs.txt}}`
