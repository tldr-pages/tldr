# tsort

> Voer een topologische sortering uit.
> Een veelvoorkomend gebruik is om de afhankelijkheidsvolgorde van knooppunten in een gerichte acyclische grafiek te tonen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tsort-invocation.html>.

- Voer een topologische sortering uit consistent met een gedeeltelijke sortering per regel van invoer gescheiden door spaties:

`tsort {{pad/naar/bestand}}`

- Voer een topologische sortering uit consistent op strings:

`echo -e "{{UI Backend\nBackend Database\nDocs UI}}" | tsort`
