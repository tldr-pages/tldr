# crane pull

> Haal externe images op via referentie en sla hun inhoud lokaal op.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

- Haal externe image op:

`crane pull {{image_naam}} {{pad/naar/tarball}}`

- Bewaar de image-referentie die is gebruikt om op te halen als een annotatie wanneer gebruikt met --format=oci:

`crane pull {{image_naam}} {{pad/naar/tarball}} --annotate-ref`

- Pad naar cache-image-lagen:

`crane pull {{image_naam}} {{pad/naar/tarball}} {{[-c|--cache_path]}} {{pad/naar/cache}}`

- Formaat waarin images moeten worden opgeslagen (standaard 'tarball'):

`crane pull {{image_naam}} {{pad/naar/tarball}} {{-format}} {{format_naam}}`

- Toon de help:

`crane pull {{[-h|--help]}}`
