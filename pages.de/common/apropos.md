# apropos

> Durchsuche die Handbuchseiten nach Namen und Beschreibungen.
> Siehe auch: `man`.
> Weitere Informationen: <https://manned.org/apropos>.

- Suche nach einem Schlüsselwort mit einem regulären Ausdruck:

`apropos {{regulären_ausdruck}}`

- Suche ohne Beschränkung der Ausgabe auf die Terminal Breite:

`apropos {{[-l|--long]}} {{regulären_ausdruck}}`

- Suche nach Seiten, die alle angegebenen Ausdrücke enthalten:

`apropos {{regulären_ausdruck_1}} {{[-a|--and]}} {{regulären_ausdruck_2}} {{[-a|--and]}} {{regulären_ausdruck_3}}`
