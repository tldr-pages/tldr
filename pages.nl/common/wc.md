# wc

> Tel regels, woorden en bytes.
> Meer informatie: <https://www.gnu.org/software/coreutils/wc>.

- Tel alle regels in een bestand:

`wc --lines {{pad/naar/bestand}}`

- Tel alle woorden in een bestand:

`wc --words {{pad/naar/bestand}}`

- Tel alle bytes in een bestand:

`wc --bytes {{pad/naar/bestand}}`

- Tel alle karakters in een bestand (rekening houdend met multi-byte karakters):

`wc --chars {{pad/naar/bestand}}`

- Tel alle regels, woorden en bytes van `stdin`:

`{{find .}} | wc`

- Tel de lengte van de langste regel in aantal karakters:

`wc --max-line-length {{pad/naar/bestand}}`
