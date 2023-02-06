# loadtest

> Futtasson terheléses tesztet a kiválasztott HTTP vagy WebSockets URL-címen. További információ: <https://github.com/alexfernandez/loadtest>.

- Futtatás egyidejű felhasználókkal és másodpercenként meghatározott számú kéréssel:

`loadtest --concurrency {{10}} --rps {{200}} {{https://example.com}}`

- Futtatás egyéni HTTP-fejléccel:

`loadtest --headers "{{accept:text/plain;text-html}}" {{https://example.com}}`

- Futtatás egy adott HTTP-módszerrel:

`loadtest --method {{GET}} {{https://example.com}}`
