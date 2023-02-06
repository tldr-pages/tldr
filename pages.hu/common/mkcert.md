# mkcert

> Eszköz a helyileg megbízható fejlesztési tanúsítványok készítéséhez. További információ: <https://github.com/FiloSottile/mkcert>.

- Telepítse a helyi hitelesítésszolgáltatót a rendszer bizalmi tárolójába:

`mkcert -install`

- Tanúsítvány és magánkulcs generálása egy adott tartományhoz:

`mkcert {{example.org}}`

- Tanúsítvány és magánkulcs generálása több tartományhoz:

`mkcert {{example.org}} {{myapp.dev}} {{127.0.0.1}}`

- Wildcard-tanúsítvány és magánkulcs generálása egy adott tartományhoz és annak aldomainjeihez:

`mkcert "{{*.example.it}}"`

- A helyi hitelesítésszolgáltató eltávolítása:

`mkcert -uninstall`
