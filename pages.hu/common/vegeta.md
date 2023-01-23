# vegeta

> Parancssori segédprogram és könyvtár a HTTP-terhelés teszteléséhez. Lásd még: `ab`. További információ: <https://github.com/tsenart/vegeta>.

- Indítson 30 másodperces támadást:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- Támadás indítása egy saját aláírású HTTPS-tanúsítvánnyal rendelkező kiszolgáló ellen:

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- Támadás indítása 10 kérés/másodperc sebességgel:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- Támadás indítása és jelentés megjelenítése:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- Indítson el egy támadást, és ábrázolja az eredményeket egy grafikonon (késleltetés az idő függvényében):

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{path/to/results.html}}`

- Támadás indítása több URL-cím ellen egy fájlból:

`vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report`
