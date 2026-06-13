# wc

> Tel regels, woorden en bytes.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Tel alle regels in een bestand:

`wc {{[-l|--lines]}} {{pad/naar/bestand}}`

- Tel alle woorden in een bestand:

`wc {{[-w|--words]}} {{pad/naar/bestand}}`

- Tel alle bytes in een bestand:

`wc {{[-c|--bytes]}} {{pad/naar/bestand}}`

- Tel alle karakters in een bestand (rekening houdend met multi-byte karakters):

`wc {{[-m|--chars]}} {{pad/naar/bestand}}`

- Tel alle regels, woorden en bytes van `stdin`:

`{{find .}} | wc`

- Tel de lengte van de langste regel in aantal karakters:

`wc {{[-L|--max-line-length]}} {{pad/naar/bestand}}`
