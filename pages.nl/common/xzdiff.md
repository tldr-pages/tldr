# xzdiff

> Roept `diff` aan op bestanden gecomprimeerd met `xz`, `lzma`, `gzip`, `bzip2`, `lzop` of `zstd`.
> Alle opgegeven opties worden direct doorgegeven aan `diff`.
> Meer informatie: <https://manned.org/xzdiff>.

- Vergelijk twee bestanden:

`xzdiff {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Vergelijk twee bestanden en toon de verschillen naast elkaar:

`xzdiff --side-by-side {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Vergelijk twee bestanden en rapporteer alleen dat ze verschillen (geen details over wat er verschilt):

`xzdiff --brief {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Vergelijk twee bestanden en rapporteer wanneer de bestanden hetzelfde zijn:

`xzdiff --report-identical-files {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Vergelijk twee bestanden met gepagineerde resultaten:

`xzdiff --paginate {{pad/naar/bestand1}} {{pad/naar/bestand2}}`
